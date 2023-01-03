
#  My Plan:
# 1. Import all that are needed.
# 2. Read in dataset.
# 3. Create analyzing functions that will:
# -- give information on the whole date frame.
# -- give information on specific column that were put in.
# -- give specific information within a column.
# 4. Create functions for plots: heatmap, histogram, 
# boxplot, boxenplot, lineplot, scatterplot, violinplot,
# subplots.
 



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from analysis_functions import *
from plotting_functions import *

hotels = pd.read_csv('hotel_bookings.csv')

# Analyzing functions

# Analyze dataframe
# Args: df, number rows - default 5
# What it will do:
# 1. print head
# 2. describe
# 3. give information
# 4. print data frame shape  
df_info(hotels)

# Analyze columns
# Args: df, list of columns
# What it will do:
# For every column it will print unique and value counts.
column_info(hotels,['hotel', 'is_canceled', 'is_repeated_guest', 'children'])

# Analyze within the column
# Args: df, column, argument as parameter
# What it will do:
# print rows with a specific command.
specific_info(hotels, 'children', 10)

#Cleaning functions

# Fill null values
# Args: df, list of columns to fill, list of filling.
# What it will do:
# fill null values in the columns with the value specified.
hotels = filling_null(hotels, ['country', 'children'], ['PRT', 0 ])


hotels = drop_columns(hotels, ['agent', 'company'])
hotels = boolean_columns(hotels, ['is_canceled', 'is_repeated_guest'])

# Plotings
create_heatmap(hotels, 'Hotel')
create_histogram(hotels, 'meal')
create_boxenplot(hotels, 'adr')
# Droping an outlier 
hotels = drop_rows(hotels, 'adr', 0, 5000)
# Continue exploring
create_boxplot(hotels, 'adr')
create_violinplot(hotels, 'meal', 'adr', 'hotel')
create_scatter(hotels, 'customer_type', 'adr')
create_lineplot(hotels, 'arrival_date_month', 'adr')
create_lineplot(hotels, 'arrival_date_month', 'adr', 'hotel')
create_displot(hotels, 'lead_time', 'hotel', 'is_canceled')
split_data(hotels, 'lead_time', 'is_canceled', 'hotel', 365)   
    
