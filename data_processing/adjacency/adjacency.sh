# arg 1 - the boundary file to process
# arg 2 - look at the attrtibute table in a GIS viewer (QGIS ect...) and find the attribute that labels regions succinctly, 
#                                                                   it will become the cell names after scenario generation
python adjacency.py "../shapefile/ontario_phu.gpkg" "PHU_ID"