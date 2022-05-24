from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback_context

df = pd.read_csv('new_covid.csv')
df.Test_Date = pd.to_datetime(df.Test_Date)
print(df.head())
df['year'] = df['Test_Date'].dt.year
df['month'] = df['Test_Date'].dt.month
df['County'] = df['County_Code']
locs = df.County_Code.tolist()
locs = locs[15:20]


def produce_group(mon, yr, df):
    filtered_df = df.loc[(df['year'] == yr) & (df['month'] == mon)]
    filtered_df = filtered_df.groupby(['year', 'month', 'County']).sum('Positive_Cases')
    return filtered_df

mar_2020 = produce_group(3, 2020, df)
apr_2020 = produce_group(4, 2020, df)
may_2020 = produce_group(5, 2020, df)
jun_2020 = produce_group(6, 2020, df)
jul_2020 = produce_group(7, 2020, df)
aug_2020 = produce_group(8, 2020, df)
sep_2020 = produce_group(9, 2020, df)
oct_2020 = produce_group(10, 2020, df)
nov_2020 = produce_group(11, 2020, df)
dec_2020 = produce_group(12, 2020, df)
jan_2021 = produce_group(1, 2021, df)
feb_2021 = produce_group(2, 2021, df)
mar_2021 = produce_group(3, 2021, df)


covid_map = Dash(__name__)
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


covid_map.layout = html.Div([
    
    dcc.Dropdown(
        id='cloropleth',
        options= [{'label': 'mar20', 'value': 'mar_2020' },
                {'label': 'apr20', 'value': 'apr_2020' },
                {'label': 'may20', 'value': 'may_2020' },
                {'label': 'jun20', 'value': 'jun_2020' },
                {'label': 'jul20', 'value': 'jul_2020' },
                {'label': 'aug20', 'value': 'aug_2020' },
                {'label': 'sep20', 'value': 'sep_2020' },
                {'label': 'oct20', 'value': 'oct_2020' },
                {'label': 'nov20', 'value': 'nov_2020' },
                {'label': 'dec20', 'value': 'dec_2020' },
                {'label': 'jan21', 'value': 'jan_2021' },
                {'label': 'feb21', 'value': 'feb_2021' },
                {'label': 'mar21', 'value': 'mar_2021' }],
        value= 'apr_2020'

    ),
    dcc.Graph(
        id='map',
        #figure=fig,
        style={'width':'120vh', 'height': '90vh'}
    )
    
    
])

@covid_map.callback(
    Output("map", "figure"),
    Input("cloropleth", "value")
)
def update_graph(value):
    print(value)
    df = mar_2020
    if value == 'apr_2020':
        df = apr_2020
    elif value == 'may_2020':
        df = may_2020
    elif value == 'jun_2020':
        df = jun_2020
    elif value == 'jul_2020':
        df = jul_2020
    elif value == 'aug_2020':
        df = aug_2020
    elif value == 'sep_2020':
        df = sep_2020
    elif value == 'oct_2020':
        df = oct_2020
    elif value == 'nov_2020':
        df = nov_2020
    elif value == 'dec_2020':
        df = dec_2020
    elif value == 'jan_2021':
        df = jan_2021
    elif value == 'feb_2021':
        df = feb_2021
    elif value == 'mar_2021':
        df = mar_2021
    fig = px.choropleth_mapbox(df, geojson=counties, locations=locs, color="Positive_Cases",
                           color_continuous_scale="Viridis",
                           range_color=(0, 30000),
                           mapbox_style="carto-positron",
                           zoom=9.2, center = {"lat": 40.7110, "lon": -73.9060},
                           opacity=0.5,
                           labels={'Positive_Cases':'Positive Cases'}
                          )
    return fig

if __name__ == '__main__':
    covid_map.run_server(debug=True)
