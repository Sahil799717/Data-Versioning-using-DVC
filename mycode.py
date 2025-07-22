import pandas as pd
import os

#Create a sample dataframe with column names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

#Ensure the directory exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

#Save the dataframe to a CSV file
df.to_csv(file_path, index=False)

#Read the CSV file back into a dataframe
print(f"Reading the CSV file to{file_path}")