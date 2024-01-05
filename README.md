1. Rename inconsistent json and jpg files (name(1).jpg and name.jpg(1).json) using `rename_json.sh`.
2. Convert timestamp in json files from UTC to local time zone using `convert_timestamp.py`.
3. List the filetypes in the library using `list_filetypes.sh`.
4. Populate DateTimeOriginal and GPS metadata from json if available using `populate_from_json.sh`.
5. Populate DateTimeOriginal from CreateDate for videos using `populate_videos.sh`.
6. Rename and move photos according to DateTimeOriginal using `rename_media.sh`
