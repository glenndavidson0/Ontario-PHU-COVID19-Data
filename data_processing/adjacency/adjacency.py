#!/usr/bin/env python
# coding: utf-8
# written by : Glenn Davidson - glenndavidson@cmail.carleton.ca

# In[36]:

import geopandas as gpd
import csv
from io import StringIO
import argparse

# In[37]:

# READ TWO ARGUMENTS FROM THE COMMAND LINE:
# 1 - the relative path+filename of the geographical boundary file
# 2 - the region id string name in the boundry file
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help= "the relative path + filename of the geographical boundary file input EX - data/canada.shp")
parser.add_argument("region_identifier", help= "the region identifier string that labels the column of geographical regions in the boundary file. EX - DAUid, PRUid, HA_NAME. These are often the offical region labels given by governmental organizations")
args = parser.parse_args()

# input shapefile
INPUT_FILE = args.input_file

# output filename
OUTPUT_FILE = "ontario_phu_adjacency.csv"

# cell id label - varies per data - name of the column that holds the region names
REGION_ID_STR = args.region_identifier

# column 1 label
REGION_ID_LABEL = "region_id"

# column 2 label
neighbor_ID_LABEL = "neighbor_id"

# read the input file into dataframe
gdf = gpd.read_file(INPUT_FILE)

# create the results file
outfile = open(OUTPUT_FILE, "w")


# In[38]:

# drop unecesscary attributes from the feature data
gdf["neighborS"] = None

for index, country in gdf.iterrows():   

    # print progress
    print("Processing Region - " + REGION_ID_STR + " = " + str(gdf.at[index, REGION_ID_STR]))
    # get 'not disjoint' countries
    nlist = gdf[~gdf.geometry.disjoint(country.geometry)][REGION_ID_STR].tolist()

    # convert this list to a list of strings from whatever data type was implicitly decided
    neighbors = list()
    for region in nlist:
        neighbors.append(str(region))
        
    # remove own name of the country from the list
    # at some point each cell is added to it's own neighborhood, should it be included here or is it inserted elsewhere?
    neighbors = [ name for name in neighbors if country[REGION_ID_STR] != name ]
    

    # add names of neighbors as neighborS value
    gdf.at[index,"neighborS"] = ", ".join(neighbors)

neighborhood_df = gpd.GeoDataFrame(gdf[[REGION_ID_STR, "neighborS"]])  


# In[39]:


neighborhood_df.head()


# In[40]:

# write the colulm labels in CSV
outfile.write(REGION_ID_LABEL + "," + neighbor_ID_LABEL + "\n")

# write the adjacency data to file in a format compadible with scenario generation
for index, region in neighborhood_df.iterrows():
    
    ## parse the name of the region
    current_region = str(region.iloc[0])
    
    ## parse the list of neighbors to array of strings
    # read the neighbor list (as a single comma seperated string)
    neighbor_str = region.iloc[1]
    
    # convert the string to list
    f = StringIO(neighbor_str)
    reader = csv.reader(f, delimiter=',')
    x = list(reader)
    neighborList = x[0]
    
    ## iterate over neighbor list and print current region,neighborlist[i]
    for neighbor in neighborList:
        neighbor = neighbor.lstrip()
        if(current_region != neighbor):
            outfile.write(current_region + "," + neighbor + "\n")
    


# In[41]:

outfile.close()
print('Done')

