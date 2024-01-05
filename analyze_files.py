"""Convert UTC timestamp to local timestamp."""
import os
import sys
from tqdm import tqdm
import exiftool

exiftool.ExifTool(executable="/home/ydobrev/Documents/pr/Image-ExifTool-12.69/exiftool")

if __name__ == "__main__":
    path = sys.argv[1]
    for root, dirs, files in os.walk(path):
        print(f"Processing {root}")
        for file in tqdm(files):
            if file.endswith(".mp4"):
                filepath = os.path.join(root, file)
                with exiftool.ExifToolHelper() as et:
                    metadata = et.get_metadata(filepath)[0]
                    for key in metadata:
                        if "DateTimeOriginal" in key:
                            if metadata[key] == "0000:00:00 00:00:00":
                                print(f'{key}: {metadata[key]}: "{filepath}"')
