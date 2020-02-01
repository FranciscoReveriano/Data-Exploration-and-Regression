import pandas as pd
import numpy as np
from tqdm import tqdm

'''Problem 1'''
# Read The Dataset
data = pd.read_csv("imports-85.data", header=None)#The .data file can be read as a .csv file

# Create the Header
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# Combine into a proper dataframe
data.columns = headers

# Print Dataset
print(data.head(5))

# Drop Unnecessary Columns
data = data.drop(columns=["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location"
                 , "engine-type", "num-of-cylinders", "fuel-system"])

# Count the number of Rows and Columns
total_rows = len(data.axes[0])
total_columns = len(data.axes[1])
print("Original Total Rows:", total_rows)
print("Original Total Columns:", total_columns)

# Convert the Price to Numerics
data["price"] = pd.to_numeric(data["price"], errors='coerce')
data = data.dropna(subset=["price"], axis = 0)
## Recount the Number of Rows and Columns
total_rows = len(data.axes[0])
total_columns = len(data.axes[1])
print("Final Total Rows:", total_rows)
print("Final Total Columns:", total_columns)
