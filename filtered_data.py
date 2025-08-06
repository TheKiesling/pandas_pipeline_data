import pandas as pd

def filter_by_city(filename: str, city: str):
    df = pd.read_csv(filename)

    filtrado = df[df['source_city'].str.contains(city)]

    print(f"\nFilas donde 'source_city' contiene '{city}':")
    print(filtrado)

    return filtrado

if __name__ == "__main__":
    filename = "extracted_files/airlines_flights_data.csv"
    filter_by_city(filename, "Delhi")
