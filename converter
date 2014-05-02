#!/usr/bin/env bash

# tool to render file acceptable for Bandcamp

# convert lossy-- add to list as needed
for file in "$(find . -regextype posix-extended -iregex ".*(mp3|ogg)")"; do
	convert "${file}" "${file}"-converted.flac
done

# convert lossless sample rate and precision as needed
for file in "$(find . -regextype posix-extended -iregex ".*(flac|wav|aiff)")"; do 
	# is sample rate high enough?
	if [ "$(soxi "${file}" | grep "Sample Rate" | awk '{ print $4 }')" -lt "44100" ]; then
		# is precision also high enough?
		if [ "$(soxi "${file}" | grep "Precision" | awk '{ gsub ( /-bit/, "" ); print $3 }')" -lt "16" ]; then
			# if no to both, then convert both
			sox "${file}" -b 16 -r 44100 "${file}"-upsampled-higher_bit.flac
		# if not precision, must be sample rate
		else
			sox "${file}" -r 44100 "${file}"-upsampled.flac
		fi
	# if sample rate is ok, check precision
	elif [ "$(soxi "${file}" | grep "Precision" | awk '{ gsub ( /-bit/, "" ); print $3 }')" -lt "16" ]; then
		sox "${file}" -b 16 "${file}"-upsampled-higher_bit.flac
	fi
done
