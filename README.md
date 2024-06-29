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

Key Insights:

- The continuous dataset covers the longest period
- Train data is split into multiple sheets, each covering a different time period
- All datasets include datetime information, allowing for time series analysis
- Weather variables are available for multiple locations
- Calendar features (holiday, school, dayOfWeek, weekend) are included

## Project Progress

### Data Preprocessing

We completed the initial data preprocessing stage:

1. **Data Loading**: All datasets (continuous-dataset, weekly-pre-dispatch-forecast, train and test dataframes) have been loaded from the `data/raw` folder.

2. **Feature Engineering**:

   - Added time-based features: hour, day_of_week, month, year, and is_weekend
   - Created lag features for demand (24, 48, and 168 hours)
   - Calculated rolling mean features for demand (24 and 168 hour windows)

3. **Data Normalization**:

   - Normalized weather columns in the continuous dataset
   - Normalized numerical columns in train and test dataframes

4. **Data Processing**:

   - Processed continuous dataset, forecast data, and individual sheets of train and test dataframes

5. **Data Storage**:
   - Saved all processed datasets in the `data/processed` directory for further analysis and modeling

### Exploratory Data Analysis (EDA)

After preprocessing the data, we performed exploratory data analysis to better understand the patterns and relationships in our dataset. The EDA process included:

1. Visualizing national demand over time
2. Analyzing the distribution of national demand
3. Examining average demand by hour of day
4. Creating a correlation heatmap of numerical features

Key findings from the EDA:

1. Correlation Analysis:

   - Strong positive correlations between temperature (T2M) variables across different locations.
   - Moderate positive correlation between national demand and temperature variables.
   - Negative correlation between national demand and weekends, indicating lower demand on weekends.

2. Distribution of National Electricity Demand:

   - Slightly right-skewed distribution.
   - Majority of demand values fall between 750 and 1500 units.
   - Presence of outliers on the lower end, potentially corresponding to anomalies or special events.

3. National Electricity Demand Over Time:

   - Clear cyclical patterns in demand, likely corresponding to daily and weekly cycles.
   - Relatively stable overall trend over the years.
   - Regular drops in demand, possibly corresponding to holidays or weekends.
   - Few significant anomalies, including a notable drop in early 2019.

4. Average Demand by Hour:
   - Lowest demand during early morning hours (2-5 AM).
   - Two peak periods: around noon and in the evening (6-8 PM).
   - Evening peak slightly higher than the midday peak.
   - Sharp rise in demand from about 6 AM, corresponding to the start of the typical workday.

Insights for Modeling:

1. Temperature and time-based features (hour, day of week, is_weekend) are likely to be important predictors.
2. Consider creating features that capture daily and weekly cycles in demand.
3. Anomalies in the data may need to be addressed through data cleaning or as a separate model component.
4. The model should be able to capture the bimodal daily pattern of demand.

The results of these analyses can be found in the `figures` directory.

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
├── figures/
│   ├── correlation_heatmap.png
│   ├── demand_distribution.png
│   ├── demand_over_time.png
│   └── hourly_demand.png
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
