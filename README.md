# Electricity Production Time Series Forecasting

## Project Overview

This project is focused on short-term electricity production forecasting using _Electricity Load Forecasting_ dataset from Kaggle. The dataset can be found [here](https://www.kaggle.com/datasets/shenba/time-series-datasets/data).

The goal is to develop and evaluate a machine learning forecasting model and compare its results with official forecasts from weekly pre-dispatch reports.

## Dataset Overview

We are using _Electricity Load Forecasting_ dataset from kaggle. More about original data sources can found on the Kaggle dataset page.

The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/electricity-load-forecasting/data) and contains the following files in the `data/raw/` directory:

1. `continuous-dataset.csv`: A CSV file containing all records in a single continuous dataset with all variables.
2. `train_dataframes.xlsx`: An Excel file containing suggested regressors and training datasets.
3. `test_dataframes.xlsx`: An Excel file containing suggested regressors and testing datasets.
4. `weekly-pre-dispatch-forecast.csv`: A CSV file containing the load forecast from weekly pre-dispatch reports.

These files provide a comprehensive set of data for training and evaluating our electricity load forecasting model.

## Project Structure

```
electricity-load-timeseries-forecast/
├── data/
│   ├── raw/
│   │   ├── continuous dataset.csv
│   │   ├── train_dataframes.xlsx
│   │   ├── test_dataframes.xlsx
│   │   └── weekly pre-dispatch forecast.csv
│   └── processed/
├── notebooks/
│   └── exploratory_data_analysis.ipynb
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── evaluation.py
├── tests/
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```
