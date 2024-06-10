import pandas as pd

# Read the CSV files
matches1 = pd.read_csv('matches1.csv')
matches2 = pd.read_csv('matches2.csv')

# Normalize column names to lowercase
matches1.columns = matches1.columns.str.lower()
matches2.columns = matches2.columns.str.lower()

# Merge the DataFrames by appending rows
merged_matches = pd.concat([matches1, matches2], ignore_index=True)

# Rename the 'Unnamed: 0' column to a space
merged_matches.rename(columns={'unnamed: 0': ''}, inplace=True)

# Save the merged DataFrame to a new CSV file
merged_matches.to_csv('matches.csv', index=False)
