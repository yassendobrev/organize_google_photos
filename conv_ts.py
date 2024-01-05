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
  timezone = TZF.timezone_at(lng=longitude, lat=latitude)
  timezone_local = pytz.timezone(timezone)
  dt_utc = datetime.datetime.fromtimestamp(timestamp)
  diff_seconds = timezone_local.utcoffset(dt_utc).total_seconds()
  return timestamp + diff_seconds

def convert_timestamp_json(filepath):
  with open(filepath, 'r+') as file:
      data = json.load(file)
      if not ("geoData" in data and \
        "latitude" in data["geoData"] and \
        "longitude" in data["geoData"]):
        return
      latitude = data["geoData"]["latitude"]
      longitude = data["geoData"]["longitude"]
      if latitude == 0 or longitude == 0:
        return

      if not ("photoTakenTime" in data and \
        "timestamp" in data["photoTakenTime"]):
        return
      timestamp_utc = int(data["photoTakenTime"]["timestamp"])
      if timestamp_utc == 0:
        return
      data["photoTakenTime"]["timestampLocal"] = \
        convert_timestamp(timestamp_utc, latitude, longitude)

  with open(filepath, 'w') as file:
      json.dump(data, file)

if __name__ == "__main__":
  path = sys.argv[1]
  for root, dirs, files in os.walk(path):
    for file in tqdm(files):
      if file.endswith('.json'):
        filepath = os.path.join(path, file)
        convert_timestamp_json(filepath)
