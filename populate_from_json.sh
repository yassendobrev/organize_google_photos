# Populate DateTimeOriginal and GPS metadata from json if available.

input_dir=$1

exiftool -r -d %s -tagsfromfile '%d/%F.json' \
  -api TimeZone='UTC' \
  '-DateTimeOriginal<PhotoTakenTimeTimestampLocal' \
  '-GPSAltitude<GeoDataAltitude' \
  '-GPSLatitude<GeoDataLatitude' \
  '-GPSLatitudeRef<GeoDataLatitude' \
  '-GPSLongitude<GeoDataLongitude' \
  '-GPSLongitudeRef<GeoDataLongitude' \
  '-Keywords<Tags' \
  '-Subject<Tags' \
  '-Caption-Abstract<Description' \
  '-ImageDescription<Description' \
  -ext '*' -overwrite_original -progress --ext json "$input_dir"
