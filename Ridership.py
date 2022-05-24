import plotly.express as px
import pandas as pd

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

df = pd.read_csv('data_reports_monthly.csv')

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
        dcc.Slider(2010, 2022, 1,
                   value=2010,
                   id='slider',
                   marks={i: '{}'.format(i) for i in range(2010, 2023)},

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
    month_dict = {1: "Jan", 2: "Feb", 3:"Mar",4:"Apr", 5:"May", 6:"Jun",7:"Jul",8:"Aug", 9:"Sep", 10:"Oct",11:"Nov",12:"Dec"}
    dff = df[pd.to_datetime(df['Month/Year']).dt.year == value]
    df_group = dff.groupby([pd.to_datetime(dff['Month/Year']).dt.month]).mean()['Trips Per Day']
    month_str = [month_dict[t] for t in df_group.index.to_list()]
        
    df_month = pd.DataFrame({'Month': month_str, 'Trips Per Day': df_group.values})
    dff1 = df_month
    # if clickData:
    #     class_filted = clickData['points'][0]['y']
    #     df_class = df[(pd.to_datetime(df['Month/Year']).dt.year == value) & (df['License Class'] == class_filted)]
    #     df_group2 = df_class.groupby([pd.to_datetime(df_class['Month/Year']).dt.month]).mean()['Trips Per Day']
    #     df_month2 = pd.DataFrame({'Month': df_group2.index, 'Trips Per Day': df_group2.values})
    #     dff1 = df_month2
    fig = px.line(dff1, x="Month", y="Trips Per Day", line_shape='spline')
    fig.update_traces(marker=dict(size=12))
    grouped = dff.groupby('License Class')['Trips Per Day'].mean()
    dff2 = pd.DataFrame({'License Class': grouped.index, 'Average Trips Per Day': grouped.values})
    horizontal_bar = px.bar(dff2, y="License Class", x="Average Trips Per Day", color="License Class")

    return None, fig, horizontal_bar


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port= 3030,debug=True)
