from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

vis = Dash(__name__)

df = pd.read_csv('Datasets/covid_test_scatter.csv')
#DATE is originally of type 'object' we convert it to type 'datetime'
df.date = pd.to_datetime(df.date)

df2 = pd.read_csv('Datasets/MTA_daily_ridership_scatter.csv')
df2.date = pd.to_datetime(df2.date)

#merge dataset on common column
df = pd.merge(df, df2, how="outer", on='date')
# some numeric values are stored as strings with commas, remove commas then convert to float
df['Subways_Total_Estimated_Ridership'] = df['Subways_Total_Estimated_Ridership'].str.replace(',','').astype(float)
print(df.info())

#we create a mask to define a date range, then we re-assign df to be the selected range defined by mask
mask = (df['date'] > '2020-03-02') & (df['date'] < '2022-03-01')
df = df.loc[mask]

##filter data by week
df_week = df[df.date.dt.weekday == 6].copy()
df_week['week'] = df_week['date'].dt.isocalendar()['week']

fig = px.scatter(df_week, x="date", y="POSITIVE_TESTS_7DAYS_AVG", 
                    size= "Subways_Percentage_of_Comparable_Pre_Pandemic_Day", hover_name = "TOTAL_TESTS_7DAYS_AVG",
                    size_max=20)

vis.layout = html.Div([
    dcc.Graph(
        id='date v pos test',
        figure=fig
    )
])

if __name__ == '__main__':
    vis.run_server(debug=True)




