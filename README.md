# Highest Profit Challenge

## Background
___

I completed the "highest-profit" challenge. The challenge was to load and clean a data.csv file and to print the number of observations before and after removing all the non-numeric data from the dataset's 'profit' column. The resulting dataframe was converted to a json file and the final assignment was to print the top 20 rows with the highest profit values. 

## Data Source
___

"data.csv" - CSV file containing corporate profits over the years

## Output
___

To run output -- click on run.bat

## Methodology:
___

Part 1:
* Imported pandas library and used the 'read_csv' function to load the data.csv file. 
* Printed the number of rows in the orginal data file by using the 'shape[0]' property -- **1st Output.** 
* Expanded dataframe using 'pd.set_option('display.max_rows', None)' to get an overall look of 'Profit' column. Observed that string "N.A." was the non-numeric column value.
* Checked that there were no nan values in 'Profit' column using 'isna()' function.
* Converted all non-numeric characters in column to nan for easier manipulation using the pandas 'to_numeric' function, and later removed all nan values with 'notnull()'function.
* Printed the total number of rows of modified dataframe after removing non-numeric values using the 'shape[0]' property -- **2nd Output.**

Part 2: 
* Converted 'Profit' column values to float type using the 'astype()' function, to facilitate the sorting of column values.
* Converted the Dataframe to JSON file using the to_json() function and created a new JSON file (data2.json) -- **3rd Output.**
* Sorted 'Profit' column values in descending order using the 'sort_values()' function.
* Printed the top 20 rows with the highest profit values, using 'head()' function. -- **4th Output.**

Part 3:
* Produced solution -- three printed output answers and a JSON file. 
