#!/usr/bin/env bash

# tool to render file acceptable for Bandcamp

if [ $# -ne 1 ]; then
	echo "Usage: $(basename $0) '/path/to/files'"
	exit 1
fi

pathtofiles=$1

# convert lossy to lossless if needed
find "${pathtofiles}" -regextype posix-extended -iregex ".*(mp3|ogg).?$" -print0 | while IFS= read -r -d $'\0' file; do
	sox "${file}" "${file}"-converted.flac
done

# convert lossless sample rate and precision as needed
find "${pathtofiles}" -regextype posix-extended -iregex ".*(flac|wav|aif).?$" -print0 | while IFS= read -r -d $'\0' file; do
	# gather info on file
	samplerate=$(soxi "${file}" | grep "Sample Rate" | awk '{ print $4 }')
	precision=$(soxi "${file}" | grep "Precision" | awk '{ gsub ( /-bit/, "" ); print $3 }') 
	# is sample rate high enough?
	if (( samplerate < 44100 )); then
		# is precision also high enough?
		if (( precision < 16 )); then
			# if no to both, then convert both
			sox "${file}" -b 16 -r 44100 "${file}"-upsampled-higher_bit.flac
		# if not precision, must be sample rate
		else
			sox "${file}" -r 44100 "${file}"-upsampled.flac
		fi
	# if sample rate is ok, check precision
	elif (( precision < 16 )); then
		sox "${file}" -b 16 "${file}"-upsampled-higher_bit.flac
	fi
done
