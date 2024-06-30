import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_processed_continuous_data():
    """Load the processed continous data"""

    return pd.read_csv('data/processed/processed_continuous.csv', parse_dates=['datetime'])

def create_cyclical_features(df, col_name, period):
    """Create sine and cosine features from datetime column"""
    df[f'{col_name}_sin'] = np.sin(2*np.pi*df[col_name]/[period])
    df[f'{col_name}_cos'] = np.cos(2*np.pi*df[col_name]/[period])

    return df

def create_lag_features(df, col_name, lags):
    """Create lag features for a given column for continuous data"""

    for lag in lags:
        df[f'{col_name}_lag_{lag}'] = df[col_name].shift(lag)

    return df

def create_rolling_features(df, col_name, windows):
    """Create rolling mean and std features for a given column"""

    for window in windows:
        df[f'{col_name}_rolling_mean_{window}'] = df[col_name].rolling(window=window).mean()
        df[f'{col_name}_rolling_std_{window}'] = df[col_name].rolling(window=window).std()

    return df

def engineer_features(df):
    """Engineer custom features including cyclical, lag, and rolling window features"""

    df = create_cyclical_features(df, 'hour', 24)
    df = create_cyclical_features(df, 'month', 12)

    df = create_lag_features(df, 'nat_demand', [24, 48, 168])

    df = create_rolling_features(df, 'nat_demand', [24, 168])

    cities = ['toc', 'san', 'dav']
    for city in cities:
        df[f'temp_humidity_interaction_{city}'] = df[f'T2M_{city}'] * df[f'QV2M_{city}']

    df['is_holiday'] = df['holiday'].astype(int)

    return df

def normalize_features(df):
    """Normalize numerical features"""
    scaler = StandardScaler()

    cols_to_norm = [col for col in df.select_dtypes(include=[np.number]).columns if not (col.startswith(('T2M_', 'QV2M_', 'TQL_', 'W2M_')) or col in ['is_weekend', 'is_holiday', 'Holiday_ID', 'school'])]

    df[cols_to_norm] = scaler.fit_transform(df[cols_to_norm])

    return df

def main():
    df = load_processed_continuous_data()
    df = engineer_features(df)
    df = normalize_features(df)
    df.to_csv('data/engineered/engineered_features.csv', index=False)

if __name__=="__main__":
    main()