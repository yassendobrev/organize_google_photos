"""Delete json files."""
import os
import sys
from tqdm import tqdm

DATA_DIR = "/mnt/ext-data1/takeout_orig/takeout"

def delete_json(json_filepath):
  """Delete json."""
  jpg_filepath = json_filepath[:-5]
  if not os.path.isfile(jpg_filepath):
    os.remove(json_filepath)
  
if __name__ == "__main__":
  subdirectory = sys.argv[1]
  path = os.path.join(DATA_DIR, subdirectory)
  for root, dirs, files in os.walk(path):
    for file in tqdm(files):
      if file.endswith('.json'):
        json_filepath = os.path.join(path, file)
        delete_json(json_filepath)
