# written by Glenn Davidson : glenndavidson@cmail.carleton.ca

# The goal of this script is to parially automate the generation of clean.csv parameters from a geograpical boundary file
# the file may not have all the required information the generate a scenario, some manual editing may be required if this script is adapted to another dataset
# the final csv should have the columns : region_id, population, area_epsg4326, region_name

# todo : fix "A value is trying to be set on a copy of a slice from a DataFrame" warning
# todo : if phu/region_id is not found in population csv then should throw error

# In[103]:
import geopandas as gpd
import pandas as pd
import csv
from copy import deepcopy

region_gdf = gpd.read_file("../shapefile/ontario_phu.gpkg")  # GeoDataFrame with the territories poligons
population_df = pd.read_csv("ontario_phu_population.csv")

# In[104]:

id_column = region_gdf["PHU_ID"]
area_column = region_gdf["Shape__Are"]
name_column = region_gdf["NAME_ENG"]

# In[105]:

clean_df = gpd.GeoDataFrame(region_gdf[["PHU_ID", "Shape__Are", "NAME_ENG"]])
clean_df.rename(columns = {'PHU_ID':'phu_id'}, inplace = True) 
clean_df.rename(columns = {'Shape__Are':'area_epsg4326'}, inplace = True) 
clean_df.rename(columns = {'NAME_ENG':'region_name'}, inplace = True) 
clean_df["population"] = 0

# In[106]:

final_df = deepcopy(clean_df)
# iterate over all PHUS and insert the population entry from population_df
for row in clean_df.iterrows():
    
    phu = row[1]["phu_id"]
    
    # find the phu in the population_df
    c = population_df["phu_gis"] == phu
    for i in range(len(c)):
        if c[i] == True :
            break
        # if never found - then should throw error
    final_df["population"][row[0]] = population_df["population"][i]  

    
# In[107]:
final_df.to_csv("ontario_phu_clean.csv")