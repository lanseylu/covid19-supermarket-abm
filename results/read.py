import pandas as pd

# Load the Parquet file
parquet_file = 'config_1000_1.parquet'

# Read the entire Parquet file into a Pandas DataFrame
df = pd.read_parquet(parquet_file)

# Calculate and print the average and standard deviation of each column except the last column
print("Average and Standard Deviation of each column except the last column:")
for column in df.columns[:-1]:  # Exclude the last column
    column_average = df[column].mean()
    column_std_dev = df[column].std()
    print(f"{column}: Average = {column_average}, Standard Deviation = {column_std_dev}")

# print(df['exposure_times'])