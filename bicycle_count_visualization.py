from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd

app = Dash(__name__)

bike_data = pd.read_csv('https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/NYC%20DOT%20Bicycle%20Count%20Data/Monthly%20Bikecount.csv')

def year_data(bikeData, year):
    bike_dataframe_year = bike_data.loc[bike_data['Year'] == year] #filters by year
    year_averages = bike_dataframe_year[['January', 'Feburary', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December' #computes the average of each column specified from the 'bike_dataframe_year' dataframe to display as rows in the 'frame' dataframe  
    ]].mean(axis = 'index') #compute average per month for all boroughs Bike data
    frame= pd.DataFrame({'Time': year_averages.index, 'Average': year_averages.values})
    fig = px.line(frame, x="Time", y="Average", title="Bike Count in NYC")
    return fig

"""Determines the bicycle count data by borough and year for the second visualization"""
def bar_graph(bikeData, borough, year):
    bike_dataframe = bike_data.loc[bike_data['Borough'] == borough] #filters by borough
    
    bike_dataframe_year = bike_dataframe.loc[bike_dataframe['Year'] == year] #filters by year

    borough_averages = bike_dataframe_year[['January', 'Feburary', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December', 'Year Average' #computes the average of each column specified from the 'bike_dataframe_year' dataframe to display as rows in the 'frame' dataframe  
    ]].mean(axis = 'index') #compute average per month for borough Bike data
    
    frame= pd.DataFrame({'Time': borough_averages.index, 'Average': borough_averages.values})

    #determines the color of bars for the second visualizations based on the borough  
    if borough == "Manhattan":
        color = ['red']
    elif borough == "Brooklyn":
        color = ['blue']
    elif borough == "Queens":
        color = ['forestgreen']
    elif borough == "Staten Island":
        color = ['purple']
    else: 
        color = ['blue']

    fig = px.bar(frame, x="Time", y="Average", title="Bike Count in " + borough, color_discrete_sequence = color)

    return fig
   
#the first visualizations which shows bike counts by borough over the years
fig = px.histogram(bike_data, x="Year", y="Year Average", color="Borough", title="Bike Count by Borough", barmode="group").update_xaxes(categoryorder='total descending')


app.layout = html.Div(children=[
    html.H1(children='NYC Department of Transportation Bike Count 2017-2021', style = {'text-align': 'center'}),

    dcc.Graph(
        id='Bike_map',
        figure=fig
    ),

    dcc.Graph(
        id='Bike_map2',
    ),
    
    dcc.Slider(
        2017, 2021, 1,
        marks={ i: '{}'.format(i) for i in range(2017, 2021)},
        value= 2017, id = "year_slider"),

    dcc.Dropdown(id = "borough", options = [
        {"label": "Manhattan", "value":"Manhattan" },  
        {"label": "Brooklyn", "value":"Brooklyn" }, 
        {"label": "Queens", "value":"Queens" },  
        {"label": "Staten Island", "value":"Staten Island" }, 
        

    ], 
        multi = False,
        value =  "Manhattan",
        style = {'width': "50%"},
        placeholder="Select a Borough to View monthly Bicycle count"
    
    ),

    dcc.Graph(
        id='Bike_map3',
    ),

    dcc.Slider(
        2017, 2021, 1,
        marks={ i: '{}'.format(i) for i in range(2017, 2021)},
        value= 2017, id = "year_slider_all_boroughs")



])


#update the main chart based on selected borough and year
@app.callback(
Output(component_id = 'Bike_map2', component_property = 'figure'), # output is the figure for the second visualization
[Input(component_id = 'borough', component_property = 'value'), #inputs are the borough and year
Input(component_id = 'year_slider', component_property = 'value')]
)

def update_main(borough, year):
    fig = bar_graph(bike_data, borough, year)
    return fig


#update the line chart based on the selected year
@app.callback(
Output(component_id = 'Bike_map3', component_property = 'figure'), # output is the figure for the second visualization
Input(component_id = 'year_slider_all_boroughs', component_property = 'value')
)

def update_line_chart(year):
    fig3 = year_data(bike_data, year)
    return fig3


if __name__ == '__main__':
    app.run_server(debug=True)