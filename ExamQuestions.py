import pandas as pd
import numpy as np


file_path = 'AQI_Data.csv'  
data = pd.read_csv(file_path)

print("Missing values before replacement:")
print(data.isnull().sum())

numeric_columns = data.select_dtypes(include=[np.number]).columns

for col in numeric_columns:
    if data[col].isnull().sum() > 0:  
        data[col] = data[col].fillna(data[col].mean())

print("\nMissing values after replacement:")
print(data.isnull().sum())


print("\nUpdated DataFrame (first 5 rows):")
print(data.head())

print("\nFirst 5 rows of the data:")
print(data.head())

print("\nLast 6 rows of the data:")
print(data.tail(6))

print("\nSummary statistics for numeric columns:")
print(data.describe())

mean_values_by_city = data.groupby('City')[['AQI', 'PM2.5', 'PM10']].mean()
print("\nMean AQI, PM2.5, and PM10 values for each city:")
print(mean_values_by_city)
5
aqi_array = data['AQI'].to_numpy()
aqi_mean = np.mean(aqi_array)
aqi_median = np.median(aqi_array)
aqi_std_dev = np.std(aqi_array)

print("\nAQI Statistics:")
print(f"Mean: {aqi_mean}")
print(f"Median: {aqi_median}")
print(f"Standard Deviation: {aqi_std_dev}")
