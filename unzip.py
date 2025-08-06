import pandas as pd
import zipfile
import os

def unzip_file(zip_path, extract_to):
    """Unzips a zip file to the specified directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)  


def read_csv_from_zip(zip_path, csv_filename):
    """Reads a CSV file from a zip archive and returns it as a DataFrame."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with zip_ref.open(csv_filename) as file:
            df = pd.read_csv(file)
    return df 

file = 'archive.zip'
extract_to = 'extracted_files'
csv_filename = 'airlines_flights_data.csv'
if not os.path.exists(extract_to):
    os.makedirs(extract_to)
unzip_file(file, extract_to)

df = read_csv_from_zip(file, csv_filename)
print(df.head())  # Display the first few rows of the DataFrame
print(df.info())  # Display information about the DataFrame
print(df.describe())  # Display summary statistics of the DataFrame
print(df.columns)