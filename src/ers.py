#!/usr/bin/env python
'''ers.py: convert radarsat 2 data to S2 format
reimplemented 20170605 from 200809 cfs aft script'''

import os
import re
import sys
from os.path import *
from fl0w3r import error, chkdir, chkfile, normpath, run, require_gdal, wopen

require_gdal()

args = sys.argv
if len(sys.argv) < 3:
    error('ers.py: Extract Radarsat-2 data to ENVI format using GDAL library.\nUsage: ers [Radarsat2 Data Directory][Output Directory]\n\nBy Ash Richardson September 2008\n')

in_dir, out_dir = args[1], args[2]

if not chkdir(in_dir):
    error('invalid input directory: ' + in_dir)

if not chkdir(out_dir):
    error('output folder does not exist: ' + out_dir)

in_dir, out_dir = normpath(in_dir), normpath(out_dir)

run('irs ' + in_dir)
run('mv ' + in_dir + 'config.txt ' + out_dir)

sf = {'s11':'HH', 's12':'HV', 's21':'VH', 's22':'VV'}

for s in sf:
    run('gdal_translate -of ENVI -ot Float32 -co INTERLEAVE=BIP ' + in_dir + 'imagery_' + sf[s] + '.tif ' + out_dir + s + '.bin')
    hfn = out_dir + s + '.hdr'
    chkfile(hfn)
    hd = open(hfn).read()
    hd = hd.replace('description = {\n', 'description = {')
    hd = hd.replace('bands   = 2', 'bands   = 1')
    hd = hd.replace('data type = 4', 'data type = 6')
    hd = hd.replace('interleave = bip', 'interleave = bsq')
    hd = hd.replace('\nband names = {\nBand 1,\nBand 2}', '')
    wopen(hfn).write(hd)
