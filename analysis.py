# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# import ebos.csv in pandas
df = pd.read_csv('ebos.csv')

# %%
# convert valid to datetime
df['valid'] = pd.to_datetime(df['valid'])
# convert tmpf from fahrenheit to celsius
df['temp_c'] = (df['tmpf'] - 32) * 5/9
# sort by valid
df = df.sort_values(by=['valid'])
# df.info()

# %%
# add column for month of year
df['month'] = df['valid'].dt.month
# add column for year
df['year'] = df['valid'].dt.year
# add column for week of year
df['week'] = df['valid'].dt.week
# add column for YYYY-WW
df['week_year'] = df['valid'].dt.strftime('%Y-%W')


# %%

df.tail()

# %%
# drop nan values
# df = df.dropna()
# drop duplicates
# df = df.drop_duplicates()

# %%
df_graph = df.copy()
# august only
df_graph = df_graph[df_graph['month'] == 8]
# only after 1980
df_graph = df_graph[df_graph['year'] >= 1980]
# group by year
df_graph = df_graph.groupby(['year']).mean()
# window size
win = 5
# moving average
df_graph['temp_c_ma'] = df_graph['temp_c'].rolling(window=win).mean()
# moving standard deviation
df_graph['temp_c_std'] = df_graph['temp_c'].rolling(window=win).std()
# moving max
df_graph['temp_c_max'] = df_graph['temp_c'].rolling(window=win).max()
# moving min
df_graph['temp_c_min'] = df_graph['temp_c'].rolling(window=win).min()
# moving slope
df_graph['temp_c_slope'] = df_graph['temp_c'].diff()
# plot temp_c
plt.figure(figsize=(12,8), dpi=160)
plt.plot(df_graph['temp_c'], label='temp_c')
plt.plot(df_graph['temp_c_ma'], label='temp_c_ma')
# plt.plot(df_graph['temp_c_std'], label='temp_c_std')
# plt.plot(df_graph['temp_c_max'], label='temp_c_max')
# plt.plot(df_graph['temp_c_min'], label='temp_c_min')
# plt.plot(df_graph['temp_c_slope'], label='temp_c_slope')
plt.legend()
plt.title('oostende_historical_weather_celsius')
plt.savefig('oostende_historical_weather_celsius.png')
plt.show()
# %%
