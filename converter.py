#!/usr/bin/env python

# py-bandcamp-converter
# a tool to render files acceptable for Bandcamp
# CC0 2014 Walter Lapchynski

import pysox
import os
import sys
import fnmatch

# Bandcamp requirements
minsamplerate = 44100.0
minprecision = 16

# extension lists
lossys = ['.mp3', '.ogg']
losslesses = ['.flac', '.wav', '.aif']

# check args
def checkArgs():
  if len(sys.argv) is not 1:
    print "Usage: " + sys.argv[0] + " '/path/to/files'"
    sys.exit(1)
  else:
    global pathtofiles = sys.argv[1]

# build matching file list
def fileList(extensionlist):
  filestoconvert = []
  for root, dirs, files in os.walk(pathtofiles):
    for file in files:
      for item in extensionlist:
        if fnmatch.fnmatch(file.lower(), "*" + item "*"):
          filestoconvert.append(os.path.join(root, file))
  return filestoconvert

# convert files
def fileConvert(filestoconvert):
  for file in filestoconvert:
    infile = pysox.CSoxStream(file)
    outfile = pysox.CSoxStream(file + "-converted.flac", "w", infile.get_signal_info())
    chain = pysox.CEffectsChain(infile, outfile)
    chain.flow_effects()
    outfile.close()

# effects chain
def fileEffect(filestoconvert)
  for file in filestoconvert:
    infile = pysox.CSoxStream(file)
    # gather info on file
    samplerate = infile.get_signal().get_signalinfo()['rate']
    precision = infile.get_signal().get_signalinfo()['precision']
    # fix sample rate and precision
    if samplerate < minsamplerate and precision < minprecision:
      outfile = pysox.CSoxStream(file + "-upsampled-higher_bit.flac", "w", pysox.CSignalInfo(minsamplerate, 2, minprecision))
    # fix precision only
    elif samplerate > minsamplerate and precision < minprecision:
      outfile = pysox.CSoxStream(file + "-higher_bit.flac", "w", pysox.CSignalInfo(samplerate, 2, minprecision))
    # fix sample rate only
    elif samplerate < minsamplerate and precision > minprecision:
      outfile = pysox.CSoxStream(file + "-upsampled.flac", "w", pysox.CSignalInfo(minsamplerate, 2, precision))
    chain = pysox.CEffectsChain(infile, outfile)
    chain.flow_effects()
    outfile.close()
    os.remove(file)

def main():
  checkArgs()
  # convert lossys
  lossyfilestoconvert = fileList(lossys)
  fileConvert(lossyfilestoconvert)
  # convert lossless
  losslessfilestoconvert = fileList(losslesses)
  fileEffect(losslessfilestoconvert)

if __name__ == '__main__':
  main()
