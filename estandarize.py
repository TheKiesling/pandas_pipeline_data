import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Estandarize:
    def __init__(self, file_type, method='zscore'):
        """
        method: 'zscore' o 'minmax'
        """
        self.file_type = file_type
        self.method    = method

    def Estandarize(self, df):
        # 2) Imputar nulos
        num_cols = df.select_dtypes(include=[np.number]).columns.drop('index', errors='ignore')
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
        cat_cols = df.select_dtypes(include=['object','category']).columns
        for c in cat_cols:
            if df[c].isna().any():
                df[c] = df[c].fillna(df[c].mode().iloc[0])

        # 3) Escalado
        if self.method=='zscore':
            std = df[num_cols].std(ddof=0)
            zero_var = std[std==0].index
            ok = std[std>0].index
            df[ok] = (df[ok] - df[ok].mean())/std[ok]
            df[zero_var] = 0.0
        elif self.method=='minmax':
            scaler = MinMaxScaler()
            df[num_cols] = scaler.fit_transform(df[num_cols])

        return df

if __name__=="__main__":
    df = pd.read_csv('extracted_files/airlines_flights_data.csv')
    est = Estandarize('csv', method='minmax')  # o method='zscore'
    df_scaled = est.Estandarize(df)
    print(df_scaled[['duration','days_left','price']].head())
