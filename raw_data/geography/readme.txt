- Boundary file included in the model_data folder
- Note in order to use this boundary file - it had to be modified by QGIS:
- PHU_ID was stored as int64 but needs to be string in scenario generation script so the conversion was made by:
    https://wiki.tuflow.com/index.php?title=QGIS_Change_Attribute_Type
- download from https://geohub.lio.gov.on.ca/datasets/ministry-of-health-public-health-unit-boundary