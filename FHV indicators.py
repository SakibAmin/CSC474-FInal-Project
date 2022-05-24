import plotly.express as px
import pandas as pd

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

df = pd.read_csv('Datasets/data_reports_monthly.csv')

df['Trips Per Day'] = (df['Trips Per Day'].str.strip()).apply(lambda x: float(x.replace(',', '')))

graph_config = dict(
    {
        "scrollZoom": True,
        "displayModeBar": True,
        "displaylogo": False,
        "modeBarButtonsToRemove": ["zoom", "zoomin", "zoomout"],
    }
)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='graph1', config=graph_config
    ),
    html.Div(
        dcc.Slider(2010, 2020, 1,
                   value=2010,
                   id='slider',
                   marks={i: '{}'.format(i) for i in range(2010, 2021)},

                   ), style={"width": "40%"}
    ),

    dcc.Graph(
        id='graph2', config=graph_config
    ),
])


@app.callback(
    Output('graph2', 'clickData'),
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Input('slider', 'value'),
    Input('graph2', 'clickData'),
)
def update_scatter(value, clickData):
    dff = df[pd.to_datetime(df['Month/Year']).dt.year == value]
    dff1 = dff
    if clickData:
        class_filted = clickData['points'][0]['y']
        dff1 = df[(pd.to_datetime(df['Month/Year']).dt.year == value) & (df['License Class'] == class_filted)]
    # if clickPoint:
    #     trace_number = clickPoint['points'][0]['curveNumber']
    #     print(dff1[(dff1['Avg Minutes Per Trip']==clickPoint['points'][0]['x'])&(dff1['Trips Per Day']==clickPoint['points'][0]['y'])]['Month/Year'].values[0])
    fig = px.scatter(dff1, x="Avg Minutes Per Trip", y="Trips Per Day", color="License Class",
                     hover_data=["Month/Year"])
    fig.update_traces(marker=dict(size=12))
    grouped = dff.groupby('License Class')['Trips Per Day'].mean()
    dff2 = pd.DataFrame({'License Class': grouped.index, 'Average Trips Per Day': grouped.values})
    horizontal_bar = px.bar(dff2, y="License Class", x="Average Trips Per Day", color="License Class")

    return None, fig, horizontal_bar


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8080,debug=True)
