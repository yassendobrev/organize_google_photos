# Rename inconsistent json and jpg files (name(1).jpg and name.jpg(1).json).

input_dir=$1

exiftool -ext json -r -if '$Filename=~/(\.[^.]+)(\(\d+\)).json$$/i' \
  '-Filename<${Filename;s/(\.[^.]+)(\(\d+\)).json$/$2$1.json/}' "$input_dir"
