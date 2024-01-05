# List the file types in the directory.

input_dir=$1

find "$input_dir" -type f | sed 's/.*\.//' | sort | uniq -c
