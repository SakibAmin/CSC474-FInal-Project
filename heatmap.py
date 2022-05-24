
import plotly.graph_objects as go
import datetime
import numpy as np
import pandas as pd


df = pd.read_csv('hosp_rate.csv')
#df.date = pd.to_datetime(df.date)
df = df.set_index('date')
print(df.info())



fig = go.Figure(data=go.Heatmap(
        z=df.values.tolist(),
        y=df.index.tolist(),
        x=df.columns.tolist(),
        colorscale='Plasma'))

fig.update_layout(
    title='Hospitalization rate per 100,000',
    xaxis_nticks=6,
    yaxis_nticks=26)

fig.show()