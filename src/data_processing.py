import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    """
    Loads all data from `raw` folder
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

# def preprocess_data(continuous_data, forecast_data):
#     """
#     Preprocess the continuous and forecast data; include:
#     1. convert date columns to `datetime`
#     2. merge the two dataframes
#     """

#     # covert the date columns to `datetime`
#     continuous_data['date'] = pd.to

def main():

    print("\nLoading datasets...")
    continuous_data, forecast_data, train_data, test_data = load_data()
    print("Done.")

    print("Summary:\n\n")
    summarize_data(continuous_data, forecast_data, train_data)
if __name__ == "__main__":
    main()