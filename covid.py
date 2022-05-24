import pandas as pd 
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback_context

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Covid vs Transportation", style={'text-align': 'center'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)