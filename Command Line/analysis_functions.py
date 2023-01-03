# Data frame information
def df_info(df, num = 5):
    print(df.head(num),
          df.columns,
          df.describe(),
          df.info(),
          df.shape)
                 
# Column information
def column_info(df, Mcolumns):
    for column in Mcolumns:
        print (df[column].unique(),
               df[column].value_counts().sort_index())

# Specific information in a column  
def specific_info(df, column, value):
    print (df[df[column]==value])

# Data cleaning by filling missing values
def filling_null(df, column_list, filling_list):
    for column, filling in zip(column_list, filling_list):
        df[column] = df[column].fillna(filling, inplace=True)
        return df

# Dropping columns
def drop_columns(df, column_list):
    for column in column_list:
        df = df.drop([column], axis = 1)
        return df

# Dropping rows out of the range
def drop_rows(df, column, num1, num2):
    df = df.loc[df[column].between(num1, num2)] 
    return df

# Turning columns into Booleans
def true_false(val):
    if val == 0:
        return False
    elif val == 1:
        return True 

# Applying Boolean functions on columns        
def boolean_columns(df, column_list):
    for column in column_list:
        df[column] = df[column].apply(true_false)
        return df
          



                  

     