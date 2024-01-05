"""Convert UTC timestamp to local timestamp."""
import datetime
import json
import pytz
import os
import sys
from timezonefinder import TimezoneFinder
from tqdm import tqdm

TZF = TimezoneFinder()


def convert_timestamp(timestamp, latitude, longitude):
    """Convert timestamp from UTC to local time."""
    # Get the photo timezone.
    timezone = TZF.timezone_at(lng=longitude, lat=latitude)
    timezone_local = pytz.timezone(timezone)

    # Get the difference between the UTC time and the time in the time zone in s.
    dt_utc = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
    dt_local = dt_utc.astimezone(timezone_local)
    diff_seconds = dt_local.utcoffset().days * 24 * 3600 + \
        dt_local.utcoffset().seconds

    # The value of timestamp_local corresponds to the local time if converted
    # assuming that it is UTC.
    timestamp_local = timestamp + diff_seconds

    return str(int(timestamp_local))


def convert_timestamp_json(filepath):
    """Populate local time field."""
    with open(filepath, "r+") as file:
        data = json.load(file)
        # Check if all required fields are present.
        if not ("geoData" in data and
                "latitude" in data["geoData"] and
                "longitude" in data["geoData"] and
                "photoTakenTime" in data and
                "timestamp" in data["photoTakenTime"]):
            return

        # Fetch and check fields.
        latitude = data["geoData"]["latitude"]
        longitude = data["geoData"]["longitude"]
        timestamp_utc = int(data["photoTakenTime"]["timestamp"])
        if (latitude == 0 and longitude == 0) or timestamp_utc == 0:
            if not ("creationTime" in data and \
                    "formatted" in data["creationTime"]):
                return
            creation_time = datetime.datetime.strptime(
                data["creationTime"]["formatted"], "%b %d, %Y, %I:%M:%S %p %Z")
            
            # Populate local time field.
            data["photoTakenTime"]["timestampLocal"] = \
                str(int(creation_time.timestamp()))
        else:
            # Populate local time field.
            data["photoTakenTime"]["timestampLocal"] = \
                convert_timestamp(timestamp_utc, latitude, longitude)

    with open(filepath, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    path = sys.argv[1]
    for root, dirs, files in os.walk(path):
        print(f"Processing {root}")
        for file in tqdm(files):
            if file.endswith(".json"):
                filepath = os.path.join(root, file)
                convert_timestamp_json(filepath)
