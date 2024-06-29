import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    """
    Loads all data from `data/raw` folder
    """

    data_dir = Path('data/raw')

    # load continuous dataset
    continuous_data = pd.read_csv(data_dir / 'continuous-dataset.csv', parse_dates=['datetime'])

    # load weekly pre-dispatch forecast
    forecast_data = pd.read_csv(data_dir / 'weekly-pre-dispatch-forecast.csv', parse_dates=['datetime'])

    # load train and test dataframes
    train_data = pd.read_excel(data_dir / 'train_dataframes.xlsx', sheet_name=None, parse_dates=['datetime'])
    test_data = pd.read_excel(data_dir / 'test_dataframes.xlsx', sheet_name=None, parse_dates=['datetime'])

    return continuous_data, forecast_data, train_data, test_data

def summarize_data(continuous_data, forecast_data, train_data):
    """
    Summary of continuous, forecast and train dataframes
    """

    print(f"----\nContinuous data samples:\n")
    print(continuous_data.head())
    print(f"----\nContinuous data info:\n")
    print(continuous_data.info())
    
    print(f"----\nForecast data samples:\n")
    print(forecast_data.head())
    print(f"----\nForecast data info:\n")
    print(forecast_data.info())

    print(f"----\nTrain data (sheet 0) samples:\n")
    print(train_data[list(train_data.keys())[0]].head())
    print(f"----\nTrain data (sheet 0) info:\n")
    print(train_data[list(train_data.keys())[0]].info())

def preprocess_continuous_data(data):
    """
    Preprocess continuous data: 
        - add 'hour', 'day_of_week', 'month', 'year', and 'is_weekend' features
        - normalize 'weather' columns
    """

    # add engineered features
    data['hour'] = data['datetime'].dt.hour
    data['day_of_week'] = data['datetime'].dt.dayofweek
    data['month'] = data['datetime'].dt.month
    data['year'] = data['datetime'].dt.year
    data['is_weekend'] = data['day_of_week'].isin([5,6]).astype(int)

    # normalize 'weather' columns
    weather_cols = ['T2M_toc', 'QV2M_toc', 'TQL_toc', 'W2M_toc', 
                    'T2M_san', 'QV2M_san', 'TQL_san', 'W2M_san',
                    'T2M_dav', 'QV2M_dav', 'TQL_dav', 'W2M_dav']
    data[weather_cols] = (data[weather_cols] - data[weather_cols].mean()) / data[weather_cols].std()
    return data

def preprocess_forecast_data(data):
    """
    Preprocess forecast data: 
        - add 'hour', 'day_of_week', 'month', 'year', and 'is_weekend' features
    """
    data['hour'] = data['datetime'].dt.hour
    data['day_of_week'] = data['datetime'].dt.dayofweek
    data['month'] = data['datetime'].dt.month
    data['year'] = data['datetime'].dt.year
    data['is_weekend'] = data['day_of_week'].isin([5,6]).astype(int)

    return data

def preprocess_train_test_data(train_data, test_data):
    """
    Preprocess train and test data:
        - train and test data contains sheets; therefore, need to be processsed individually
    """

    processed_train = {}
    processed_test = {}

    for sheet_name, data in train_data.items():
        processed_train[sheet_name] = preprocess_sheet(data, f"train_{sheet_name}")

    for sheet_name, data in test_data.items():
        processed_test[sheet_name] = preprocess_sheet(data, f'test_{sheet_name}')

    return processed_train, processed_test
    
def preprocess_sheet(data, sheet_name):
    """Preprocess individual sheets"""
    # create lag features
    for lag in [24, 48, 168]:
        data[f'demain_lag_{lag}'] = data['DEMAND'].shift(lag)
    
    # create rolling mean features
    for window in [24, 168]:
        data[f'demand_rolling_mean_{window}'] = data['DEMAND'].rolling(window=window).mean()
    
    # normalize numerical columns
    numerical_cols = ['week_X-2', 'week_X-3', 'week_X-4', 'MA_X-4', 'T2M_toc']
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean())/data[numerical_cols].std()

    # convert 'weekend to int
    data['weekend'] = data['weekend'].astype(int)

    return data



def main():

    print("\nLoading datasets...")
    continuous_data, forecast_data, train_data, test_data = load_data()
    print("Done.")

    # print("Summary:\n\n")
    # summarize_data(continuous_data, forecast_data, train_data)

    print("Preprocessing data...")
    print("Preprocessing continous data...")
    processed_continuous_data = preprocess_continuous_data(continuous_data)
    print("Preprocessing forecast data...")
    processed_forecast_data = preprocess_forecast_data(forecast_data)
    print("Preprocessing train and test data...")
    processed_train_data, processed_test_data = preprocess_train_test_data(train_data, test_data)

    # save the processed data to 'data/processed' dir
    print("Saving processed data...")
    processed_continuous_data.to_csv('data/processed/processed_continuous.csv', index=False)
    processed_forecast_data.to_csv('data/processed/processed_forecast.csv', index=False)

    for sheet_name, data in processed_train_data.items():
        data.to_csv(f'data/processed_train_{sheet_name}.csv', index=False)
    
    for sheet_name, data in processed_test_data.items():
        data.to_csv(f'data/processed_test_{sheet_name}.csv', index=False)
    
    print("Processed data saved to 'data/processed'")

if __name__ == "__main__":
    main()