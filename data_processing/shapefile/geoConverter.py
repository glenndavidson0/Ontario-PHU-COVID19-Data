#!/usr/bin/env python
# coding: utf-8
# written by : Glenn Davidson - glenndavidson@cmail.carleton.ca
# Geographical Boundary File Converter using geopandas
# Conversion from geojson to shp and gpkg needs to be tested more, saw some odd behaviour

# Command Line Arguments:
# 1 - the input filename
# 2 - the output filename
# 3 - the output file type / geopandas driver
# 4 - target crs if any conversion is required

# In[36]:

import geopandas as gpd
import csv
from io import StringIO
import argparse
import sys

# In[37]:
# create parser and parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help = "the relative path + filename of the input boundary file")
parser.add_argument("outputfile", help = "the relative path + filename of the output file")
parser.add_argument("format", help = "the format of the output boundary file (should match extension of outputfile) - geojson, gpkg, shp")
parser.add_argument("crs", help = "The coordinate system the output file")
args = parser.parse_args()
INPUT_FILE = args.inputfile 
OUTPUT_FILE = args.outputfile 
FORMAT = args.format 
CRS = args.crs 

# set driver format string
if(FORMAT == "geojson"):
    driver_str = "GeoJSON"
elif(FORMAT == "gpkg"):
    driver_str = "GPKG"
elif(FORMAT == "shp"):
    driver_str = "none"
else:
    sys.exit("Incorrect format flag: see --help")

# set CRS conversion flag
if(CRS == "same"):
    convert_crs = False
else:
    convert_crs = True

# read input boundary file
gdf = gpd.read_file(INPUT_FILE)
print("input file CRS is:")
print(gdf.crs)

# do crs conversion
if convert_crs:
    gdf = gdf.to_crs(CRS)

# output the file
if(driver_str == "none"):
    gdf.to_file(OUTPUT_FILE)
else:
    gdf.to_file(OUTPUT_FILE, driver=driver_str)

