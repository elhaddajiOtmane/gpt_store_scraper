# First, let's load the first 100 items from the CSV file using pandas to check the contents.

import pandas as pd

# Path to the CSV file
file_path = '/mnt/data/GPTs_Details.csv'

# Read the first 100 rows
data = pd.read_csv(file_path, nrows=100)
data.head()
