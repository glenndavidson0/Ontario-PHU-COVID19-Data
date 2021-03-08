# written by:
# glenndavidson@cmail.carleton.ca
# glenntdavidson@gmail.com

import geopandas as gpd
gdf = gpd.read_file("../geography/Ministry_of_Health_Public_Health_Unit_Boundary.shp")
print("shp CRS was:")
print(gdf.crs)
gdf = gdf.to_crs("EPSG:4326")
print("CRS for GPKG is:")
print(gdf.crs)
gdf.to_file("output/output.gpkg", driver="GPKG")