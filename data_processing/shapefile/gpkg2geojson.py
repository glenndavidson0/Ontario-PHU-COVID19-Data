# written by:
# glenndavidson@cmail.carleton.ca
# glenntdavidson@gmail.com

import geopandas as gpd
gdf = gpd.read_file("ontario_phu.gpkg")
print("shp CRS was:")
print(gdf.crs)
gdf = gdf.to_crs("EPSG:4326")
print("CRS for GeoJSON is:")
print(gdf.crs)
gdf.to_file("ontario_phu.geojson", driver='GeoJSON')
