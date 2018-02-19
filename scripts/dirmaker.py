
import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point, Polygon
import os
import re
import zipfile,fnmatch

import sys

# SET CITY NAME
# CITIES = ["amsterdam","munich","oslo","barcelona","berlin","london","ams","paris","rome","stockholm","milan"]
CITIES = ["wien"]
# Base directory
BASE_DIR = os.path.abspath(".")
# base directory for data files
BASE_DIR_DATA = os.path.join(BASE_DIR, "data")
directoriesToBuild = ['clipped','mapped','tessellation','osm_raw','foursquare_raw','train','dev','test','count', 'landuse']
# build folder structure for each city
def makeDirStruct(city):
    for directory in directoriesToBuild:
        if not os.path.exists(os.path.join(BASE_DIR_DATA,city,directory)):
            os.makedirs(os.path.join(BASE_DIR_DATA,city,directory))
# create directories and unzip files
for CITY_NAME in CITIES:
    makeDirStruct(CITY_NAME)


