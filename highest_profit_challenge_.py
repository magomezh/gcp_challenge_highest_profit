
# importing pandas library
import pandas as pd


# ## Part 1

# Loading csv file into pandas 
df = pd.read_csv("data.csv")
df.head()


# Taking a look at 'Profit' column values, 'N.A.' seems be the non-numeric value in 'Profit' column
pd.set_option('display.max_rows', None)
df


# Printing number of rows in original data file
print(f'Number of rows in data.csv file: {df.shape[0]}')


# checking for column names
df.columns


# Checking for nan values in 'profit' column
df['Profit (in millions)'].isna().sum()


# Converting all non-numeric characters in column to nan for easier manipulation, and removing all nan values
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
df_2 = df[pd.to_numeric(df['Profit (in millions)'], errors='coerce').notnull()]


# Comparing number of rows after removing nan values with original dataframe
df.shape, df_2.shape

# Printing number of rows in dataframe after removing non-numeric values
print(f'Number of rows in dataframe after removing non-numeric values: {df_2.shape[0]}')


# ## Part 2

df_2.dtypes  # Checking data types for each column
df_2['Profit (in millions)'] = df_2['Profit (in millions)'].astype(float) # Converting 'Profit' column values to float type
df_2.dtypes # Rechecking data type of 'Profit Column', to faciliate sorting


# creating a jason file, data2.json
df_2.to_json(r'data2.json', orient="records",  indent = 3)


# Printing top 20 rows with highest profit values
sorted_df = df_2.sort_values(by=['Profit (in millions)'], ascending=False)
print(sorted_df.head(20))



