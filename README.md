# Portafoglio

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat) 
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Linux-blue?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)


## Description

The project, loads datas from yahoo finance (using the library requests), that return a file csv with heading.
From this csv, use some functions to convert the csv to json and yaml starting from the dictionary


## Requirements

- Python version between `3.6` and `3.9`
- `requests` library
  ```commandline
  pip install requests
  ```
- `csv` library
  ```commandline
  pip install csv
  ```
- `pandas` library
  ```commandline
  pip install pandas
  ```
- `json` library
  ```commandline
  pip install json
  ```

## Execution

Open a terminal with path "./portafoglio/" and type the following command:

- Windows:
  ```
  python main.py
  ```

- Linux:
  ```
  python3 main.py
  ```


## Group

- mattiaambrosi
- kleinleon
- saramarcolini
- RiccardoVillardi


## Progress

##### 29/01/2023

- Convert from csv to yaml
- Test the program
- Documentation

##### 28/01/2023

- Made a function to get csv file from Yahoo Finance
- Create dictionary containing the csv data
- Convert from csv to json
