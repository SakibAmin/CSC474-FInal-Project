
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd

app = Dash(__name__)

""" reads the 'CitiBike Trips 2017-2022.csv' to refer to citibike trips per month by year. This information is displayed as a line chart"""

data = pd.read_csv("..\\Datasets\\CitiBike Data\\CitiBike Trips 2017-2022.csv")


fig = px.line(data, x="Month", y="Ridership Trip Count", color= "Year",  title="CitiBike Trips Count in NYC by month from 2017-2022")


app.layout = html.Div(children=[
    html.H1(children='NYC CitiBike Trips count 2017-2022', style = {'text-align': 'center'}),

    dcc.Graph(
        id='Bike_map',
        figure=fig
    ),
]
)

if __name__ == '__main__':
    app.run_server(debug=True)