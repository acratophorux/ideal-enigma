# Electricity Load Forecasting

## Project Overview

This project is focused on short-term electricity load forecasting using _Electricity Load Forecasting_ dataset from Kaggle. The dataset can be found [here](https://www.kaggle.com/datasets/shenba/time-series-datasets/data).

The goal is to develop and evaluate a machine learning forecasting model and compare its results with official forecasts from weekly pre-dispatch reports.

## Dataset Overview

We are using _Electricity Load Forecasting_ dataset from kaggle. More about original data sources can found on the Kaggle dataset page.

The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/electricity-load-forecasting/data) and contains the following files in the `data/raw/` directory:

1. `continuous-dataset.csv`:

   - 48,048 entries
   - 17 columns including datetime, national demand, weather variables for three locations (toc, san, dav), and calendar information
   - Key features: datetime, nat*demand, T2M*\_, QV2M\_\_, TQL*\*, W2M*\*, Holiday_ID, holiday, school

2. `weekly-pre-dispatch-forecast.csv`:

   - 40,152 entries
   - 2 columns: datetime and load_forecast

3. `train_dataframes.xlsx`:

   - 14 sheets with varying numbers of entries:
   - Each sheet contains 12 columns including datetime, historical demand (week_X-2, week_X-3, week_X-4), moving average, calendar features, temperature, and actual demand
   - The increasing number of entries per sheet suggests that each sheet covers a progressively larger time period

4. `test_dataframes.xlsx`:
   - Structure similar to train_dataframes.xlsx

Key Points:

- The continuous dataset covers the longest period
- Train data is split into multiple sheets, each covering a different time period
- All datasets include datetime information, allowing for time series analysis
- Weather variables are available for multiple locations
- Calendar features (holiday, school, dayOfWeek, weekend) are included

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
│   └── eda.ipynb
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
