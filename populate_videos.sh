# Populate DateTimeOriginal from CreateDate for videos.

input_dir=$1

exiftool -ext 'mp4' --ext 'json' -r -progress -overwrite_original \
  "-DateTimeOriginal<CreateDate" \
  "$input_dir" 
