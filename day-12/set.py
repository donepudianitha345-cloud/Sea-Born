import pandas as pd
import numpy as np


df = pd.read_csv('property_data.csv')


df['price_per_sqft'] = (df['price'] / df['size_sqft']).round(2)


df['date_listed'] = pd.to_datetime(df['date_listed'])
df['listing_month'] = df['date_listed'].dt.month


df['is_new_construction'] = np.where(df['year_built'] >= 2020, 1, 0)
print("--- Transformed Data ---")
print(df)


