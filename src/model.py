import pandas as pd
from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error
from statsmodels.tsa.ar_model import AutoReg
import xgboost as xgb

def load_engineered_data():
    """
    Load engineered data from 'data/engineered'
    """

    data_dir = Path('data/engineered/engineered_features.csv')

    return pd.read_csv(data_dir, parse_dates=['datetime'])

def prepare_data(df, target_col='nat_demand', test_size=0.2):
    """Prepare data from modeling (train and test split)"""

    df = df.sort_values('datetime') 
    df.set_index('datetime', inplace=True)

    X = df.drop([target_col], axis=1)
    y = df[target_col]

    split_point = int(len(df) * (1 - test_size))
    X_train, X_test = X[:split_point], X[split_point:]
    y_train, y_test = y[:split_point], y[split_point:]

    return X_train, X_test, y_train, y_test

def train_autoregressive_model(y_train, lags=24):
    """Train autoreg"""

    model = AutoReg(y_train, lags=lags)
    model_fit = model.fit()
    return model_fit

def train_xgboost_model(X_train, y_train):
    """Train XGBoost"""
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
    model.fit(X_train, y_train)
    return model

def evaluate_model(y_true, y_pred):
    """Model evaluation and performance"""
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    return {"MSE": mse, "RMSE": rmse, "MAE":mae}

def main():
    df = load_engineered_data()

    X_train, X_test, y_train, y_test = prepare_data(df)

    autoreg_model = train_autoregressive_model(y_train)
    autoreg_pred = autoreg_model.forecast(steps=len(y_test))
    autoreg_metrics = evaluate_model(y_test, autoreg_pred)
    print("Autoregressive Model Metrics:", autoreg_metrics)

    xgb_model = train_xgboost_model(X_train, y_train)
    xgb_pred = xgb_model.predict(X_test)
    xgb_metrics = evaluate_model(y_test, xgb_pred)
    print("XGBoost Model Metrics:", xgb_metrics)


    feature_importance = pd.DataFrame({
        'feature':X_train.columns,
        'importance': xgb_model.feature_importances_
    }).sort_values('importance', ascending=False)

    print("\nTop 10 Important Features:")
    print(feature_importance.head(10))


if __name__=="__main__":
    main()