# Rename and move photos according to DateTimeOriginal.

input_dir=$1
output_dir=$2

exiftool '-FileName<DateTimeOriginal' \
  -ext '*' --ext 'json' -r -progress \
  -d "$output_dir/%Y/%m/%Y-%m-%d_%H.%M.%S%%-c.%%le" \
  "$input_dir" 
