bandcamp-converter
=====================

WARNING: nausea is a common side effect of using this software if you are an audiofile.

Yes, transcoding and upsampling is nasty. This is the joy of Bandcamp it requires high quality lossless uploads, so any derivative is proportionally good quality. 

However, as a netlabel owner that uses Bandcamp as a primary means of distribution, I've found a lot of musicians are NOT audiophiles. Surprising, but true. After many hours trying to convince and train people on how to make high quality recordings, I've given up for the most part. If It's not easy for them to fix, I'll just convert it. 

This tool makes that process super easy. It will convert lossy files to flac if necessary and make sure all audio files have have at least 16-bit precision and 44.1kHz sample rate.

Makes use out of the [pysox](https://pythonhosted.org/pysox/) library. If you don't have it already:
``` sh
$ sudo apt-get update
$ sudo apt-get -y install python-pip libsox-dev python-dev
$ sudo pip install --pre pysox
```

Usage: 
``` sh
$ python converter.py '/path/to/files'
```

If you prefer the non-Python version, then:
``` sh
$ converter.sh '/path/to/files'
```
