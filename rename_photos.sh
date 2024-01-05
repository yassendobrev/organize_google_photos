# Rename and move photos according to DateTimeOriginal.

input_dir="/mnt/ext-data1/takeout_orig/takeout"
output_dir="/mnt/ext-data1/takeout_orig/takeout_mod"

subdir=$1

echo "$input_dir/$subdir"

exiftool '-FileName<DateTimeOriginal' \
  -ext '*' --ext 'json' -r -progress \
  -d "$output_dir/%Y/%m/%Y-%m-%d_%H.%M.%S%%-c.%%le" \
  "$input_dir/$subdir" 
