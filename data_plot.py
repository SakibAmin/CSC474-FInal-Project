import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

df=pd.read_csv('https://raw.githubusercontent.com/Hulkgrinder/cardata/main/car_ridership.csv')
df_2019=df.loc[df["Year"]==2019]
df_2020=df.loc[df["Year"]==2020]
df_2021=df.loc[df["Year"]==2021]
print(df_2019)
fig_color_line=px.line(df_2019
            ,x = 'Month'
            ,y = 'Trips Per Month'
            ,color = 'License Class',
            title="Private Ridership For 2019"
            )
fig_color_line.show()
fig_color_scat = px.scatter(df_2020, x="Month", y="Trips Per Month", color="License Class", symbol="species", title="Private Ridership For 2020")
fig_color_scat.show()
fig_color_bar = px.bar(df_2021, x="Month", y="Trips Per Month", color="License Class", title="Private Ridership For 2021")
fig_color_bar.show()