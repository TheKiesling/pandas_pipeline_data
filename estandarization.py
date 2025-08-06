import pandas as pd
from sklearn.preprocessing import StandardScaler

def estandarizar_dataset(df):
    columnas_categoricas = ['airline', 'source_city', 'destination_city',
                            'departure_time', 'arrival_time', 'stops', 'class']
    
    for col in columnas_categoricas:
        df[col] = df[col].str.strip().str.lower()

    # One-Hot Encoding 
    df = pd.get_dummies(df, columns=columnas_categoricas, drop_first=True)

    # Estandarización de columnas numéricas
    columnas_numericas = ['duration', 'days_left', 'price']
    scaler = StandardScaler()
    df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])

    return df
