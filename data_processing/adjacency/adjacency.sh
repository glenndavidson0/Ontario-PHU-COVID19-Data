# arg 1 - the boundary file to process
# arg 2 - look at the attrtibute table in a GIS viewer (QGIS ect...) and find the attribute that labels regions succinctly, 
#                                                                   it will become the cell names aftr scenario generation
python adjacency.py "../../raw_data/geography/Ministry_of_Health_Public_Health_Unit_Boundary.shp" "PHU_ID"