Ontario Public Health Unit COVID-19 Dataset
===

***Description:***
This repository contains one publicly available COVID-19 dataset for the Geography-Based-SEIRDS model
https://github.com/glenndavidson0/Geography-Based-SERIDS

***What a raw dataset contains:***
- A Geographical Boundary File for the specified area.
- Population counts within the regions of the geographical file.
- The COVID-19 case numbers in each region per day starting in 2020.

***What a model dataset contains:***
- A Geographical Boundary File for the specified area (properly formatted)
- A *clean.csv which contains region id, region population, region area, and region name
- an *adjacency.csv which contains information on which regions share borders for neighborhood generation

This repository contains tools to process raw datasets, scenario generation, and example files from the process output:
- data_processing : scripts used to process raw data
- model_data : the output of the data_processing stage
- raw_data : the publicly available COVID-19 data
- scenario_generation : uses the outputs of data_processing stage that are copied to the model data folder to generate a scenario

The contents of the model_data folder may be used directly with the scenario generation tool and the SEIRDS model without running the data processing tools.
