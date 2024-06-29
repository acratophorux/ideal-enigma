import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
def load_processed_data():
    """Load the processed continuous data"""

    data_dir = Path('data/processed/processed_continuous.csv')
    return pd.read_csv(data_dir, parse_dates=['datetime'])

def plot_demand_over_time(data):
    """Plot the national demand over time"""

    plt.figure(figsize=(15,6))
    plt.plot(data['datetime'], data['nat_demand'])
    plt.title('National Electricity Demand Over Time')
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.savefig('figures/demand_over_time.png')
    plt.close()

def plot_demand_distribution(data):
    """
    Plot the distribution of national demand
    """
    plt.figure(figsize=(10,6))
    sns.histplot(data['nat_demand'], kde=True)
    plt.title('Distribution of National Electricity Demand')
    plt.xlabel("Demand")
    plt.savefig('figures/demand_distribution.png')
    plt.close()

def plot_demand_by_hour(data):
    """Plot average demand by hour"""
    hourly_demand = data.groupby('hour')['nat_demand'].mean()
    
    plt.figure(figsize=(10,6))
    hourly_demand.plot(kind='bar')
    plt.title("Average Demand by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Demand")
    plt.savefig("figures/hourly_demand.png")
    plt.close()

def plot_correlation_heatmap(data):
    """Plot correlation heatmap of numerical features"""
    corr = data.select_dtypes(include=[np.number]).corr()

    plt.figure(figsize=(12,12))
    sns.heatmap(corr, annot=False, cmap='coolwarm')
    plt.title('Correlation Heatmap of Numerical Features')
    plt.savefig('figures/correlation_heatmap.png')
    plt.close()



def main():
    data = load_processed_data()
    # print(data[data['nat_demand'] <= 600])
    
    plot_demand_over_time(data)
    plot_demand_distribution(data)
    plot_correlation_heatmap(data)
    plot_demand_by_hour(data)


if __name__=="__main__":
    main()