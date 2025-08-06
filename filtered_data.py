import pandas as pd

filename = 'extracted_files/airlines_flights_data.csv'

df = pd.read_csv(filename)

print(df.columns)

print(df[df['source_city'].str.contains("Delhi")])