import pandas as pd 
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback_context
import json
from urllib.request import urlopen

app = Dash(__name__)

#MTA Dataset
mtadf = pd.read_csv("Datasets/MTA_daily_ridership.csv")

#2022 MTA Data
data2022 = mtadf[mtadf["Year"] == 2022]

Jan2022 = data2022[data2022["Month"] == 1]
Feb2022 = data2022[data2022["Month"] == 2]
Mar2022 = data2022[data2022["Month"] == 3]
April2022 = data2022[data2022["Month"] == 4]
May2022 = data2022[data2022["Month"] == 5]
June2022 = data2022[data2022["Month"] == 6]
July2022 = data2022[data2022["Month"] == 7]
Aug2022 = data2022[data2022["Month"] == 8]
Sep2022 = data2022[data2022["Month"] == 9]
Oct2022 = data2022[data2022["Month"] == 10]
Nov2022 = data2022[data2022["Month"] == 11]
Dec2022 = data2022[data2022["Month"] == 12]

subJan2022 = Jan2022['Subways_Total_Estimated_Ridership'].sum()
subFeb2022 = Feb2022['Subways_Total_Estimated_Ridership'].sum()
subMar2022 = Mar2022['Subways_Total_Estimated_Ridership'].sum()
subApril2022 = April2022['Subways_Total_Estimated_Ridership'].sum()
subMay2022 = May2022['Subways_Total_Estimated_Ridership'].sum()
subJune2022 = June2022['Subways_Total_Estimated_Ridership'].sum()
subJuly2022 = July2022['Subways_Total_Estimated_Ridership'].sum()
subAug2022 = Aug2022['Subways_Total_Estimated_Ridership'].sum()
subSep2022 = Sep2022['Subways_Total_Estimated_Ridership'].sum()
subOct2022 = Oct2022['Subways_Total_Estimated_Ridership'].sum()
subNov2022 = Nov2022['Subways_Total_Estimated_Ridership'].sum()
subDec2022 = Dec2022['Subways_Total_Estimated_Ridership'].sum()


busJan2022 = Jan2022['Buses_Total_Estimated_Ridership'].sum()
busFeb2022 = Feb2022['Buses_Total_Estimated_Ridership'].sum()
busMar2022 = Mar2022['Buses_Total_Estimated_Ridership'].sum()
busApril2022 = April2022['Buses_Total_Estimated_Ridership'].sum()
busMay2022 = May2022['Buses_Total_Estimated_Ridership'].sum()
busJune2022 = June2022['Buses_Total_Estimated_Ridership'].sum()
busJuly2022 = July2022['Buses_Total_Estimated_Ridership'].sum()
busAug2022 = Aug2022['Buses_Total_Estimated_Ridership'].sum()
busSep2022 = Sep2022['Buses_Total_Estimated_Ridership'].sum()
busOct2022 = Oct2022['Buses_Total_Estimated_Ridership'].sum()
busNov2022 = Nov2022['Buses_Total_Estimated_Ridership'].sum()
busDec2022 = Dec2022['Buses_Total_Estimated_Ridership'].sum()


data2022 = {'Year': [2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Subway': [ subJan2022, subFeb2022, subMar2022, subApril2022, subMay2022, subJune2022, subJuly2022, subAug2022, subSep2022, subOct2022, subNov2022, subDec2022],
            'Bus': [busJan2022, busFeb2022, busMar2022, busApril2022, busMay2022, busJune2022, busJuly2022, busAug2022, busSep2022, busOct2022, busNov2022, busDec2022]
            }

df2022 = pd.DataFrame(data2022)
#print(df2022)

#2021 MTA Data
data2021 = mtadf[mtadf["Year"] == 2021]

Jan2021 = data2021[data2021["Month"] == 1]
Feb2021 = data2021[data2021["Month"] == 2]
Mar2021 = data2021[data2021["Month"] == 3]
April2021 = data2021[data2021["Month"] == 4]
May2021 = data2021[data2021["Month"] == 5]
June2021 = data2021[data2021["Month"] == 6]
July2021 = data2021[data2021["Month"] == 7]
Aug2021 = data2021[data2021["Month"] == 8]
Sep2021 = data2021[data2021["Month"] == 9]
Oct2021 = data2021[data2021["Month"] == 10]
Nov2021 = data2021[data2021["Month"] == 11]
Dec2021 = data2021[data2021["Month"] == 12]

subJan2021 = Jan2021['Subways_Total_Estimated_Ridership'].sum()
subFeb2021 = Feb2021['Subways_Total_Estimated_Ridership'].sum()
subMar2021 = Mar2021['Subways_Total_Estimated_Ridership'].sum()
subApril2021 = April2021['Subways_Total_Estimated_Ridership'].sum()
subMay2021 = May2021['Subways_Total_Estimated_Ridership'].sum()
subJune2021 = June2021['Subways_Total_Estimated_Ridership'].sum()
subJuly2021 = July2021['Subways_Total_Estimated_Ridership'].sum()
subAug2021 = Aug2021['Subways_Total_Estimated_Ridership'].sum()
subSep2021 = Sep2021['Subways_Total_Estimated_Ridership'].sum()
subOct2021 = Oct2021['Subways_Total_Estimated_Ridership'].sum()
subNov2021 = Nov2021['Subways_Total_Estimated_Ridership'].sum()
subDec2021 = Dec2021['Subways_Total_Estimated_Ridership'].sum()

busJan2021 = Jan2021['Buses_Total_Estimated_Ridership'].sum()
busFeb2021 = Feb2021['Buses_Total_Estimated_Ridership'].sum()
busMar2021 = Mar2021['Buses_Total_Estimated_Ridership'].sum()
busApril2021 = April2021['Buses_Total_Estimated_Ridership'].sum()
busMay2021 = May2021['Buses_Total_Estimated_Ridership'].sum()
busJune2021 = June2021['Buses_Total_Estimated_Ridership'].sum()
busJuly2021 = July2021['Buses_Total_Estimated_Ridership'].sum()
busAug2021 = Aug2021['Buses_Total_Estimated_Ridership'].sum()
busSep2021 = Sep2021['Buses_Total_Estimated_Ridership'].sum()
busOct2021 = Oct2021['Buses_Total_Estimated_Ridership'].sum()
busNov2021 = Nov2021['Buses_Total_Estimated_Ridership'].sum()
busDec2021 = Dec2021['Buses_Total_Estimated_Ridership'].sum()

data2021 = {'Year': [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Subway': [ subJan2021, subFeb2021, subMar2021, subApril2021, subMay2021, subJune2021, subJuly2021, subAug2021, subSep2021, subOct2021, subNov2021, subDec2021],
            'Bus': [busJan2021, busFeb2021, busMar2021, busApril2021, busMay2021, busJune2021, busJuly2021, busAug2021, busSep2021, busOct2021, busNov2021, busDec2021]
            }

df2021 = pd.DataFrame(data2021)
#print(df2021)

#2020 MTA Data
data2020 = mtadf[mtadf["Year"] == 2020]

Jan2020 = data2020[data2020["Month"] == 1]
Feb2020 = data2020[data2020["Month"] == 2]
Mar2020 = data2020[data2020["Month"] == 3]
April2020 = data2020[data2020["Month"] == 4]
May2020 = data2020[data2020["Month"] == 5]
June2020 = data2020[data2020["Month"] == 6]
July2020 = data2020[data2020["Month"] == 7]
Aug2020 = data2020[data2020["Month"] == 8]
Sep2020 = data2020[data2020["Month"] == 9]
Oct2020 = data2020[data2020["Month"] == 10]
Nov2020 = data2020[data2020["Month"] == 11]
Dec2020 = data2020[data2020["Month"] == 12]


subJan2020 = Jan2020['Subways_Total_Estimated_Ridership'].sum()
subFeb2020 = Feb2020['Subways_Total_Estimated_Ridership'].sum()
subMar2020 = Mar2020['Subways_Total_Estimated_Ridership'].sum()
subApril2020 = April2020['Subways_Total_Estimated_Ridership'].sum()
subMay2020 = May2020['Subways_Total_Estimated_Ridership'].sum()
subJune2020 = June2020['Subways_Total_Estimated_Ridership'].sum()
subJuly2020 = July2020['Subways_Total_Estimated_Ridership'].sum()
subAug2020 = Aug2020['Subways_Total_Estimated_Ridership'].sum()
subSep2020 = Sep2020['Subways_Total_Estimated_Ridership'].sum()
subOct2020 = Oct2020['Subways_Total_Estimated_Ridership'].sum()
subNov2020 = Nov2020['Subways_Total_Estimated_Ridership'].sum()
subDec2020 = Dec2020['Subways_Total_Estimated_Ridership'].sum()


busJan2020 = Jan2020['Buses_Total_Estimated_Ridership'].sum()
busFeb2020 = Feb2020['Buses_Total_Estimated_Ridership'].sum()
busMar2020 = Mar2020['Buses_Total_Estimated_Ridership'].sum()
busApril2020 = April2020['Buses_Total_Estimated_Ridership'].sum()
busMay2020 = May2020['Buses_Total_Estimated_Ridership'].sum()
busJune2020 = June2020['Buses_Total_Estimated_Ridership'].sum()
busJuly2020 = July2020['Buses_Total_Estimated_Ridership'].sum()
busAug2020 = Aug2020['Buses_Total_Estimated_Ridership'].sum()
busSep2020 = Sep2020['Buses_Total_Estimated_Ridership'].sum()
busOct2020 = Oct2020['Buses_Total_Estimated_Ridership'].sum()
busNov2020 = Nov2020['Buses_Total_Estimated_Ridership'].sum()
busDec2020 = Dec2020['Buses_Total_Estimated_Ridership'].sum()

data2020 = {'Year': [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Subway': [ subJan2020, subFeb2020, subMar2020, subApril2020, subMay2020, subJune2020, subJuly2020, subAug2020, subSep2020, subOct2020, subNov2020, subDec2020],
            'Bus': [busJan2020, busFeb2020, busMar2020, busApril2020, busMay2020, busJune2020, busJuly2020, busAug2020, busSep2020, busOct2020, busNov2020, busDec2020]
            }

df2020 = pd.DataFrame(data2020)
#print(df2020)

#Merging MTA DataFrames
frames = [df2022,df2021,df2020]
mtadff = pd.concat(frames)

#Covid Dataset
df = pd.read_csv("Datasets/covid_test.csv")

#2020 Covid Data
covidData2020 = df[df["Year"] == 2020]

covidJan2020 = covidData2020[covidData2020["Month"] == 1]
covidFeb2020 = covidData2020[covidData2020["Month"] == 2]
covidMar2020 = covidData2020[covidData2020["Month"] == 3]
covidApril2020 = covidData2020[covidData2020["Month"] == 4]
covidMay2020 = covidData2020[covidData2020["Month"] == 5]
covidJune2020 = covidData2020[covidData2020["Month"] == 6]
covidJuly2020 = covidData2020[covidData2020["Month"] == 7]
covidAug2020 = covidData2020[covidData2020["Month"] == 8]
covidSep2020 = covidData2020[covidData2020["Month"] == 9]
covidOct2020 = covidData2020[covidData2020["Month"] == 10]
covidNov2020 = covidData2020[covidData2020["Month"] == 11]
covidDec2020 = covidData2020[covidData2020["Month"] == 12]

Janpert = 0
Febpert = 0

Martotal = covidMar2020["TOTAL_TESTS"].sum()
Marpostive = covidMar2020["POSITIVE_TESTS"].sum()
Marpert = (Marpostive / Martotal)*100

Apriltotal = covidApril2020["TOTAL_TESTS"].sum()
Aprilpostive = covidApril2020["POSITIVE_TESTS"].sum()
Aprilpert = (Aprilpostive / Apriltotal)*100

Maytotal = covidMay2020["TOTAL_TESTS"].sum()
Maypostive = covidMay2020["POSITIVE_TESTS"].sum()
Maypert = (Maypostive / Maytotal)*100

Junetotal = covidJune2020["TOTAL_TESTS"].sum()
Junepostive = covidJune2020["POSITIVE_TESTS"].sum()
Junepert = (Junepostive / Junetotal)*100

Julytotal = covidJuly2020["TOTAL_TESTS"].sum()
Julypostive = covidJuly2020["POSITIVE_TESTS"].sum()
Julypert = (Julypostive / Julytotal)*100

Augtotal = covidAug2020["TOTAL_TESTS"].sum()
Augpostive = covidAug2020["POSITIVE_TESTS"].sum()
Augpert = (Augpostive / Augtotal)*100

Septotal = covidSep2020["TOTAL_TESTS"].sum()
Seppostive = covidSep2020["POSITIVE_TESTS"].sum()
Seppert = (Seppostive / Septotal)*100

Octtotal = covidOct2020["TOTAL_TESTS"].sum()
Octpostive = covidOct2020["POSITIVE_TESTS"].sum()
Octpert = (Octpostive / Octtotal)*100

Novtotal = covidNov2020["TOTAL_TESTS"].sum()
Novpostive = covidNov2020["POSITIVE_TESTS"].sum()
Novpert = (Novpostive / Novtotal)*100

Dectotal = covidDec2020["TOTAL_TESTS"].sum()
Decpostive = covidDec2020["POSITIVE_TESTS"].sum()
Decpert = (Decpostive / Dectotal)*100

covidData2020 = {'Year': [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Covid': [Janpert, Febpert, Marpert, Aprilpert, Maypert, Junepert, Julypert, Augpert, Seppert, Octpert, Novpert, Decpert],
            }

dfcovid2020 = pd.DataFrame(covidData2020)
#print(dfcovid2020)

#2021 Covid Data
covidData2021 = df[df["Year"] == 2021]

covidJan2021 = covidData2021[covidData2021["Month"] == 1]
covidFeb2021 = covidData2021[covidData2021["Month"] == 2]
covidMar2021 = covidData2021[covidData2021["Month"] == 3]
covidApril2021 = covidData2021[covidData2021["Month"] == 4]
covidMay2021 = covidData2021[covidData2021["Month"] == 5]
covidJune2021 = covidData2021[covidData2021["Month"] == 6]
covidJuly2021 = covidData2021[covidData2021["Month"] == 7]
covidAug2021 = covidData2021[covidData2021["Month"] == 8]
covidSep2021 = covidData2021[covidData2021["Month"] == 9]
covidOct2021 = covidData2021[covidData2021["Month"] == 10]
covidNov2021 = covidData2021[covidData2021["Month"] == 11]
covidDec2021 = covidData2021[covidData2021["Month"] == 12]

Jantotal = covidJan2021["TOTAL_TESTS"].sum()
Janpostive = covidJan2021["POSITIVE_TESTS"].sum()
Janpert = (Janpostive / Jantotal)*100

Febtotal = covidFeb2021["TOTAL_TESTS"].sum()
Febpostive = covidFeb2021["POSITIVE_TESTS"].sum()
Febpert = (Febpostive / Febtotal)*100

Martotal = covidMar2021["TOTAL_TESTS"].sum()
Marpostive = covidMar2021["POSITIVE_TESTS"].sum()
Marpert = (Marpostive / Martotal)*100

Apriltotal = covidApril2021["TOTAL_TESTS"].sum()
Aprilpostive = covidApril2021["POSITIVE_TESTS"].sum()
Aprilpert = (Aprilpostive / Apriltotal)*100

Maytotal = covidMay2021["TOTAL_TESTS"].sum()
Maypostive = covidMay2021["POSITIVE_TESTS"].sum()
Maypert = (Maypostive / Maytotal)*100

Junetotal = covidJune2021["TOTAL_TESTS"].sum()
Junepostive = covidJune2021["POSITIVE_TESTS"].sum()
Junepert = (Junepostive / Junetotal)*100

Julytotal = covidJuly2021["TOTAL_TESTS"].sum()
Julypostive = covidJuly2021["POSITIVE_TESTS"].sum()
Julypert = (Julypostive / Julytotal)*100

Augtotal = covidAug2021["TOTAL_TESTS"].sum()
Augpostive = covidAug2021["POSITIVE_TESTS"].sum()
Augpert = (Augpostive / Augtotal)*100

Septotal = covidSep2021["TOTAL_TESTS"].sum()
Seppostive = covidSep2021["POSITIVE_TESTS"].sum()
Seppert = (Seppostive / Septotal)*100

Octtotal = covidOct2021["TOTAL_TESTS"].sum()
Octpostive = covidOct2021["POSITIVE_TESTS"].sum()
Octpert = (Octpostive / Octtotal)*100

Novtotal = covidNov2021["TOTAL_TESTS"].sum()
Novpostive = covidNov2021["POSITIVE_TESTS"].sum()
Novpert = (Novpostive / Novtotal)*100

Dectotal = covidDec2021["TOTAL_TESTS"].sum()
Decpostive = covidDec2021["POSITIVE_TESTS"].sum()
Decpert = (Decpostive / Dectotal)*100

covidData2021 = {'Year': [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Covid': [Janpert, Febpert, Marpert, Aprilpert, Maypert, Junepert, Julypert, Augpert, Seppert, Octpert, Novpert, Decpert],
            }

dfcovid2021 = pd.DataFrame(covidData2021)
#print(dfcovid2021)

#2022 Covid Data
covidData2022 = df[df["Year"] == 2022]

covidJan2022 = covidData2022[covidData2022["Month"] == 1]
covidFeb2022 = covidData2022[covidData2022["Month"] == 2]
covidMar2022 = covidData2022[covidData2022["Month"] == 3]
covidApril2022 = covidData2022[covidData2022["Month"] == 4]
covidMay2022 = covidData2022[covidData2022["Month"] == 5]
covidJune2022 = covidData2022[covidData2022["Month"] == 6]
covidJuly2022 = covidData2022[covidData2022["Month"] == 7]
covidAug2022 = covidData2022[covidData2022["Month"] == 8]
covidSep2022 = covidData2022[covidData2022["Month"] == 9]
covidOct2022 = covidData2022[covidData2022["Month"] == 10]
covidNov2022 = covidData2022[covidData2022["Month"] == 11]
covidDec2022 = covidData2022[covidData2022["Month"] == 12]

Jantotal = covidJan2022["TOTAL_TESTS"].sum()
Janpostive = covidJan2022["POSITIVE_TESTS"].sum()
Janpert = (Janpostive / Jantotal)*100

Febtotal = covidFeb2022["TOTAL_TESTS"].sum()
Febpostive = covidFeb2022["POSITIVE_TESTS"].sum()
Febpert = (Febpostive / Febtotal)*100

Martotal = covidMar2022["TOTAL_TESTS"].sum()
Marpostive = covidMar2022["POSITIVE_TESTS"].sum()
Marpert = (Marpostive / Martotal)*100

Apriltotal = covidApril2022["TOTAL_TESTS"].sum()
Aprilpostive = covidApril2022["POSITIVE_TESTS"].sum()
Aprilpert = (Aprilpostive / Apriltotal)*100

Maytotal = covidMay2022["TOTAL_TESTS"].sum()
Maypostive = covidMay2022["POSITIVE_TESTS"].sum()
Maypert = (Maypostive / Maytotal)*100

Junepert = 0
Julypert = 0
Augpert = 0
Seppert = 0
Octpert = 0
Novpert = 0
Decpert = 0

covidData2022 = {'Year': [2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Covid': [Janpert, Febpert, Marpert, Aprilpert, Maypert, Junepert, Julypert, Augpert, Seppert, Octpert, Novpert, Decpert],
            }

dfcovid2022 = pd.DataFrame(covidData2022)
#print(dfcovid2022)

#Merging Covid Data
frames = [dfcovid2022,dfcovid2021,dfcovid2020]
coviddff = pd.concat(frames)

#Covid Map Data
df = pd.read_csv('Datasets/new_covid.csv')
df.Test_Date = pd.to_datetime(df.Test_Date)
#print(df.head())
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

#Covid Scatter Plot Data

dfscat = pd.read_csv('Datasets/covid_test_scatter.csv')
dfscat.date = pd.to_datetime(dfscat.date)

dfscat2 = pd.read_csv('Datasets/MTA_daily_ridership_scatter.csv')
dfscat2.date = pd.to_datetime(dfscat2.date)


dfscat = pd.merge(dfscat, dfscat2, how="outer", on='date')
dfscat['Subways_Total_Estimated_Ridership'] = dfscat['Subways_Total_Estimated_Ridership'].str.replace(',','').astype(float)

mask = (dfscat['date'] > '2020-03-02') & (dfscat['date'] < '2022-03-01')
dfscat = dfscat.loc[mask]


df_week = dfscat[dfscat.date.dt.weekday == 6].copy()
df_week['week'] = df_week['date'].dt.isocalendar()['week']


#Covid HeatMap
dfheat = pd.read_csv('Datasets/hosp_rate.csv')
dfheat = dfheat.set_index('date')

#Covid Matrix Graph Data
mask2 = (dfscat['date'] > '2020-03-02') & (dfscat['date'] < '2021-04-01')
dfscatm = dfscat.loc[mask2]



#CitiBike Line Graph Data
df1 = pd.read_csv('Datasets/CitiBike Trips 2017-2022.csv')

#2022 Car Data
df2 = pd.read_csv("Datasets/Car_dataset.csv")

cardata2022 = df2[df2["Year"] == 2022]

Jandata = cardata2022[cardata2022["Month"] == 'January']
Febdata = cardata2022[cardata2022["Month"] == 'February']
Mardata = cardata2022[cardata2022["Month"] == 'March']
Aprildata = cardata2022[cardata2022["Month"] == 'April']
Maydata = cardata2022[cardata2022["Month"] == 'May']
Junedata = cardata2022[cardata2022["Month"] == 'June']
Julydata = cardata2022[cardata2022["Month"] == 'July']
Augdata = cardata2022[cardata2022["Month"] == 'August']
Sepdata = cardata2022[cardata2022["Month"] == 'September']
Octdata = cardata2022[cardata2022["Month"] == 'October']
Novdata = cardata2022[cardata2022["Month"] == 'November']
Decdata = cardata2022[cardata2022["Month"] == 'December']

Jantotal = Jandata["Trips Per Month"].sum()
Febtotal = Febdata["Trips Per Month"].sum()
Martotal = Mardata["Trips Per Month"].sum()
Apriltotal = Aprildata["Trips Per Month"].sum()
Maytotal = Maydata["Trips Per Month"].sum()
Junetotal = Junedata["Trips Per Month"].sum()
Julytotal = Julydata["Trips Per Month"].sum()
Augtotal = Augdata["Trips Per Month"].sum()
Septotal = Sepdata["Trips Per Month"].sum()
Octtotal = Octdata["Trips Per Month"].sum()
Novtotal = Novdata["Trips Per Month"].sum()
Dectotal = Decdata["Trips Per Month"].sum()

cdata2022 = {'Year': [2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022,2022],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Car': [Jantotal, Febtotal, Martotal, Apriltotal, Maytotal, Junetotal, Julytotal, Augtotal, Septotal, Octtotal, Novtotal, Dectotal],
            }

dfcardata2022 = pd.DataFrame(cdata2022)

#2021 Car Data
cardata2021 = df2[df2["Year"] == 2021]

Jandata = cardata2021[cardata2021["Month"] == 'January']
Febdata = cardata2021[cardata2021["Month"] == 'February']
Mardata = cardata2021[cardata2021["Month"] == 'March']
Aprildata = cardata2021[cardata2021["Month"] == 'April']
Maydata = cardata2021[cardata2021["Month"] == 'May']
Junedata = cardata2021[cardata2021["Month"] == 'June']
Julydata = cardata2021[cardata2021["Month"] == 'July']
Augdata = cardata2021[cardata2021["Month"] == 'August']
Sepdata = cardata2021[cardata2021["Month"] == 'September']
Octdata = cardata2021[cardata2021["Month"] == 'October']
Novdata = cardata2021[cardata2021["Month"] == 'November']
Decdata = cardata2021[cardata2021["Month"] == 'December']

Jantotal = Jandata["Trips Per Month"].sum()
Febtotal = Febdata["Trips Per Month"].sum()
Martotal = Mardata["Trips Per Month"].sum()
Apriltotal = Aprildata["Trips Per Month"].sum()
Maytotal = Maydata["Trips Per Month"].sum()
Junetotal = Junedata["Trips Per Month"].sum()
Julytotal = Julydata["Trips Per Month"].sum()
Augtotal = Augdata["Trips Per Month"].sum()
Septotal = Sepdata["Trips Per Month"].sum()
Octtotal = Octdata["Trips Per Month"].sum()
Novtotal = Novdata["Trips Per Month"].sum()
Dectotal = Decdata["Trips Per Month"].sum()

cdata2021 = {'Year': [2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021,2021],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Car': [Jantotal, Febtotal, Martotal, Apriltotal, Maytotal, Junetotal, Julytotal, Augtotal, Septotal, Octtotal, Novtotal, Dectotal],
            }

dfcardata2021 = pd.DataFrame(cdata2021)

#2020 Car Data
cardata2020 = df2[df2["Year"] == 2020]

Jandata = cardata2020[cardata2020["Month"] == 'January']
Febdata = cardata2020[cardata2020["Month"] == 'February']
Mardata = cardata2020[cardata2020["Month"] == 'March']
Aprildata = cardata2020[cardata2020["Month"] == 'April']
Maydata = cardata2020[cardata2020["Month"] == 'May']
Junedata = cardata2020[cardata2020["Month"] == 'June']
Julydata = cardata2020[cardata2020["Month"] == 'July']
Augdata = cardata2020[cardata2020["Month"] == 'August']
Sepdata = cardata2020[cardata2020["Month"] == 'September']
Octdata = cardata2020[cardata2020["Month"] == 'October']
Novdata = cardata2020[cardata2020["Month"] == 'November']
Decdata = cardata2020[cardata2020["Month"] == 'December']

Jantotal = Jandata["Trips Per Month"].sum()
Febtotal = Febdata["Trips Per Month"].sum()
Martotal = Mardata["Trips Per Month"].sum()
Apriltotal = Aprildata["Trips Per Month"].sum()
Maytotal = Maydata["Trips Per Month"].sum()
Junetotal = Junedata["Trips Per Month"].sum()
Julytotal = Julydata["Trips Per Month"].sum()
Augtotal = Augdata["Trips Per Month"].sum()
Septotal = Sepdata["Trips Per Month"].sum()
Octtotal = Octdata["Trips Per Month"].sum()
Novtotal = Novdata["Trips Per Month"].sum()
Dectotal = Decdata["Trips Per Month"].sum()

cdata2020 = {'Year': [2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020],
            'Month': ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"],
            'Car': [Jantotal, Febtotal, Martotal, Apriltotal, Maytotal, Junetotal, Julytotal, Augtotal, Septotal, Octtotal, Novtotal, Dectotal],
            }

dfcardata2020 = pd.DataFrame(cdata2020)

#MTA Total Ridership
dfmta = pd.read_csv("Datasets/Bus Total Ridership.csv",dtype={"FIPS_Code": str})
mask = dfmta["Borough"]

#Merging Car Datasets
frames = [dfcardata2020,dfcardata2021,dfcardata2022]
cardff = pd.concat(frames)

#Train Chlorpleth Map Dataset
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("Datasets/subway_ridership_total.csv")
locs = [36005, 36081, 36047, 36061, 36085]

#2020
bronx = df[df["FIPS"] == 36005]
bronxtotal = bronx["2020"].sum()

queens = df[df["FIPS"] == 36081]
queenstotal = queens["2020"].sum()

brooklyn = df[df["FIPS"] == 36047]
brooklyntotal = brooklyn["2020"].sum()

manhattan = df[df["FIPS"] == 36061]
manhattantotal = manhattan["2020"].sum()

si = df[df["FIPS"] == 36085]
sitotal = si["2020"].sum()

data2020 = {
            'FIPS': [36005, 36081, 36047, 36061, 36085],
            'Borough': ["Bronx", "Queens", "Brooklyn", "Manhattan", "Staten Island"],
            'Ridership': [bronxtotal, queenstotal, brooklyntotal, manhattantotal, sitotal],
            'Year': [2020, 2020, 2020, 2020, 2020]
            }
dftraindata2020 = pd.DataFrame(data2020)

#2019
bronx = df[df["FIPS"] == 36005]
bronxtotal = bronx["2019"].sum()

queens = df[df["FIPS"] == 36081]
queenstotal = queens["2019"].sum()

brooklyn = df[df["FIPS"] == 36047]
brooklyntotal = brooklyn["2019"].sum()

manhattan = df[df["FIPS"] == 36061]
manhattantotal = manhattan["2019"].sum()

si = df[df["FIPS"] == 36085]
sitotal = si["2019"].sum()

data2019 = {
            'FIPS': [36005, 36081, 36047, 36061, 36085],
            'Borough': ["Bronx", "Queens", "Brooklyn", "Manhattan", "Staten Island"],
            'Ridership': [bronxtotal, queenstotal, brooklyntotal, manhattantotal, sitotal],
            'Year': [2019, 2019, 2019, 2019, 2019]
            }
dfdatatrain2019 = pd.DataFrame(data2019)

frames = [dfdatatrain2019,dftraindata2020]
dftraindata = pd.concat(frames)

#Bus Dataset
df = pd.read_csv("Datasets/bus ridership Annual Total.csv")
locs = [36005, 36081, 36047, 36061, 36085]
bronx = df[df["FIPS"] == 36005]
bronxtotal = bronx["2020"].sum()

queens = df[df["FIPS"] == 36081]
queenstotal = queens["2020"].sum()

brooklyn = df[df["FIPS"] == 36047]
brooklyntotal = brooklyn["2020"].sum()

manhattan = df[df["FIPS"] == 36061]
manhattantotal = manhattan["2020"].sum()

si = df[df["FIPS"] == 36085]
sitotal = si["2020"].sum()

data2020 = {
            'FIPS': [36005, 36081, 36047, 36061, 36085],
            'Borough': ["Bronx", "Queens", "Brooklyn", "Manhattan", "Staten Island"],
            'Ridership': [bronxtotal, queenstotal, brooklyntotal, manhattantotal, sitotal],
            'Year': [2020, 2020, 2020, 2020, 2020]
            }
dfbusdata2020 = pd.DataFrame(data2020)

#2019
bronx = df[df["FIPS"] == 36005]
bronxtotal = bronx["2019"].sum()

queens = df[df["FIPS"] == 36081]
queenstotal = queens["2019"].sum()

brooklyn = df[df["FIPS"] == 36047]
brooklyntotal = brooklyn["2019"].sum()

manhattan = df[df["FIPS"] == 36061]
manhattantotal = manhattan["2019"].sum()

si = df[df["FIPS"] == 36085]
sitotal = si["2019"].sum()

data2019 = {
            'FIPS': [36005, 36081, 36047, 36061, 36085],
            'Borough': ["Bronx", "Queens", "Brooklyn", "Manhattan", "Staten Island"],
            'Ridership': [bronxtotal, queenstotal, brooklyntotal, manhattantotal, sitotal],
            'Year': [2019, 2019, 2019, 2019, 2019]
            }
dfbusdata2019 = pd.DataFrame(data2019)

frames = [dfbusdata2019,dfbusdata2020]
dfbusdata = pd.concat(frames)

#Bike Dataset

bike_data = pd.read_csv('Datasets/Monthly Bikecount.csv')

def year_dataframe(bikeData, year):
    bike_dataframe_year = bike_data.loc[bike_data['Year'] == year] #filters by year
    year_averages = bike_dataframe_year[['January', 'Feburary', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December' #computes the average of each column specified from the 'bike_dataframe_year' dataframe to display as rows in the 'frame' dataframe  
    ]].mean(axis = 'index') #compute average per month for all boroughs Bike data
    frame= pd.DataFrame({'Time': year_averages.index, 'Average': year_averages.values})
    yearlist = [year] * 12
    frame["Year"] = yearlist
    #print(frame)
    return frame

data_2017 = year_dataframe(bike_data, 2017)
data_2018 = year_dataframe(bike_data, 2018)
data_2019 = year_dataframe(bike_data, 2019)
data_2020 = year_dataframe(bike_data, 2020)
data_2021 = year_dataframe(bike_data, 2021)

years_list = [data_2017, data_2018, data_2019, data_2020, data_2021]
years_dataframe= pd.concat(years_list)

bike_dataframe_year = bike_data.loc[bike_data['Year'] == 'year'] #filters by year
year_averages = bike_dataframe_year[['January', 'Feburary', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December' #computes the average of each column specified from the 'bike_dataframe_year' dataframe to display as rows in the 'frame' dataframe  
]].mean(axis = 'index') #compute average per month for all boroughs Bike data
frame= pd.DataFrame({'Time': year_averages.index, 'Average': year_averages.values})

df=pd.read_csv('https://raw.githubusercontent.com/Hulkgrinder/cardata/main/car_ridership.csv')
df_2019=df.loc[df["Year"]==2019]
df_2020=df.loc[df["Year"]==2020]
df_2021=df.loc[df["Year"]==2021]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#App Layout
dcc.Location(id='url', refresh=False),
app.layout = html.Div([

    html.H1("Covid19 vs Transportation", style={'text-align': 'center'}),

    #Covid Map Dropdown
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
        value= 'mar_2020'

    ),
    dcc.Graph(id='map', style={'width':'120vh', 'height': '90vh'}
    ),

    #Line Graph Dropdown
    dcc.Dropdown(id="mta_select_year",
                 options=[
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021},
                     {"label": "2022", "value": 2022}],
                 multi=False,
                 value=2020,
                 style={'width': "40%"}
                 ),

    #LineGraphs
    dcc.Graph(id='covid_graph', figure={}),
    dcc.Graph(id='mta_subway_graph', figure={}),
    dcc.Graph(id='mta_bus_graph', figure={}),
    dcc.Graph(id='bike_graph', figure={}),
    dcc.Graph(id='car_graph', figure={}),

    #Buttons
    html.Button('Covid', id='covid_button', n_clicks=0, style={'text-align': 'center', 'font-size': '12px', 'width': '140px', 'height': '25px'}),
    html.Button('Train', id='train_button', n_clicks=0, style={'text-align': 'center', 'font-size': '12px', 'width': '140px', 'height': '25px'}),
    html.Button('Bus', id='bus_button', n_clicks=0, style={'text-align': 'center', 'font-size': '12px', 'width': '140px', 'height': '25px'}),
    html.Button('Bike', id='bike_button', n_clicks=0, style={'text-align': 'center', 'font-size': '12px', 'width': '140px', 'height': '25px'}),
    html.Button('Car', id='car_button', n_clicks=0, style={'text-align': 'center', 'font-size': '12px', 'width': '140px', 'height': '25px'}),

    #Graphs inside the buttons
    dcc.Graph(id='Graph_1', figure={}),
    dcc.Graph(id='Graph_2', figure={}),
    dcc.Graph(id='Graph_3', figure={}),

])
@app.callback(
    Output("map", "figure"),
    Input("cloropleth", "value")
)
def update_map(value):
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
    figgy = px.choropleth_mapbox(df, geojson=counties, locations=locs, color="Positive_Cases",
                           color_continuous_scale="Viridis",
                           range_color=(0, 30000),
                           mapbox_style="carto-positron",
                           zoom=9.2, center = {"lat": 40.7110, "lon": -73.9060},
                           opacity=0.5,
                           labels={'Positive_Cases':'Positive Cases'}
                          )
    return figgy

@app.callback(
     Output(component_id='covid_graph', component_property='figure'),
     Output(component_id='mta_subway_graph', component_property='figure'),
     Output(component_id='mta_bus_graph', component_property='figure'),
     Output(component_id='bike_graph', component_property='figure'),
     Output(component_id='car_graph', component_property='figure'),
     Input(component_id='mta_select_year', component_property='value'),
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))
    dff = mtadff.copy()
    dff = dff[dff["Year"] == option_slctd]

    cdff = coviddff.copy()
    cdff = cdff[cdff["Year"] == option_slctd]

    dff1 = df1.copy()
    dff1 = dff1[dff1["Year"] == option_slctd]
        
    dff2 = cardff.copy()
    dff2 = dff2[dff2["Year"] == option_slctd]

    fig = px.line(cdff, x='Month', y="Covid", title="Percentage Postive Covid Cases")
    fig1= px.line(dff, x='Month', y="Subway", title="Train Ridership")
    fig2 = px.line(dff, x='Month', y="Bus", title="Bus Ridership")
    fig3 = px.line(dff1, x="Month", y="Ridership Trip Count", title="Bike Ridership")
    fig4 = px.line(dff2, x="Month", y="Car", title="Car Ridership")

    return fig, fig1, fig2, fig3, fig4

@app.callback(
    Output(component_id='Graph_1', component_property='figure'),
    Output(component_id='Graph_2', component_property='figure'),
    Output(component_id='Graph_3', component_property='figure'),
    Input('covid_button', component_property='n_clicks'),
    Input('train_button', component_property='n_clicks'),
    Input('bus_button', component_property='n_clicks'),
    Input('bike_button', component_property='n_clicks'),
    Input('car_button', component_property='n_clicks'),
)

def update_button(covid_clicks, train_clicks, bus_clicks, bike_clicks, car_clicks):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    fig5 = px.scatter(df_week, x="date", y="POSITIVE_TESTS_7DAYS_AVG", 
                    size= "Subways_Percentage_of_Comparable_Pre_Pandemic_Day", hover_name = "TOTAL_TESTS_7DAYS_AVG",
                    size_max=20)

    fig6 = go.Figure(data=go.Heatmap(
        z=dfheat.values.tolist(),
        y=dfheat.index.tolist(),
        x=dfheat.columns.tolist(),
        colorscale='Plasma'))

    fig6.update_layout(
            title='Hospitalization rate per 100,000',
            xaxis_nticks=6,
            yaxis_nticks=26)
        
    fig7 = px.scatter_matrix(dfscatm,
            dimensions=["TOTAL_TESTS_7DAYS_AVG", "POSITIVE_TESTS_7DAYS_AVG", "PERCENT_POSITIVE_7DAYS_AVG" ],
            color="Subways_Total_Estimated_Ridership",
            labels={
                    "TOTAL_TESTS_7DAYS_AVG": "Total tests",
                    "POSITIVE_TESTS_7DAYS_AVG":"Positive tests",
                    "PERCENT_POSITIVE_7DAYS_AVG": "% positive",
                    "Subways_Total_Estimated_Ridership": "Subway ridership"
                    },
            title = "7 Day testing averages & subway ridership"
                    )

    if 'covid_button' in changed_id:
        
        fig5 = px.scatter(df_week, x="date", y="POSITIVE_TESTS_7DAYS_AVG", 
                    size= "Subways_Percentage_of_Comparable_Pre_Pandemic_Day", hover_name = "TOTAL_TESTS_7DAYS_AVG",
                    size_max=20)

        fig6 = go.Figure(data=go.Heatmap(
        z=dfheat.values.tolist(),
        y=dfheat.index.tolist(),
        x=dfheat.columns.tolist(),
        colorscale='Plasma'))

        fig6.update_layout(
            title='Hospitalization rate per 100,000',
            xaxis_nticks=6,
            yaxis_nticks=26)
        
        fig7 = px.scatter_matrix(dfscatm,
            dimensions=["TOTAL_TESTS_7DAYS_AVG", "POSITIVE_TESTS_7DAYS_AVG", "PERCENT_POSITIVE_7DAYS_AVG" ],
            color="Subways_Total_Estimated_Ridership",
            labels={
                    "TOTAL_TESTS_7DAYS_AVG": "Total tests",
                    "POSITIVE_TESTS_7DAYS_AVG":"Positive tests",
                    "PERCENT_POSITIVE_7DAYS_AVG": "% positive",
                    "Subways_Total_Estimated_Ridership": "Subway ridership"
                    },
            title = "7 Day testing averages & subway ridership"
                    )

    if 'train_button' in changed_id:
        fig5 = go.Figure(data=[
            go.Bar(name='2018', x=mask, y=[2428768,897346,6030487,1520105,0,10876533]),
            go.Bar(name='2019', x=mask, y=[2426912,892042,6138177,1530940,0,10988070]),
            go.Bar(name='2020', x=mask, y=[903681,388840,1899099,596340,0,3787960,]),
        ])
        fig5.update_layout(title= 'Train Ridership Totals Per Borough', barmode='group')

        dffmap = dftraindata.copy()
        dffmap = dffmap[dffmap["Year"] == 2020]

        fig6 = px.choropleth_mapbox(dffmap, geojson=counties, locations=locs, color = 'Ridership',
                           color_continuous_scale="Viridis",
                           range_color=(0, 300000000),
                           mapbox_style="carto-positron",
                           zoom=9.2, center = {"lat": 40.7110, "lon": -73.9060},
                           opacity=0.5
                           #labels={'':'Positive Cases'}
                          )
        fig6.update_layout(
            title='2020 Train Ridership Map')
        
        dffmap2 = dftraindata.copy()
        dffmap2 = dffmap2[dffmap2["Year"] == 2019]
        fig7 = px.choropleth_mapbox(dffmap2, geojson=counties, locations=locs, color = 'Ridership',
                           color_continuous_scale="Viridis",
                           range_color=(0, 300000000),
                           mapbox_style="carto-positron",
                           zoom=9.2, center = {"lat": 40.7110, "lon": -73.9060},
                           opacity=0.5
                           #labels={'':'Positive Cases'}
                          )
        fig7.update_layout(
            title='2019 Train Ridership Map')
 

    if 'bus_button' in changed_id:
        fig5 = go.Figure(data=[
            go.Bar(name='2018', x=mask, y=[1396941,1226032,1169618,1148777,349328,4003796]),
            go.Bar(name='2019', x=mask, y=[1192082,904924,802781,1396727,216152,4515334]),
            go.Bar(name='2020', x=mask, y=[714222,589706,389852,800079,128479,2623350])
        ])
        fig5.update_layout(title= 'Bus Ridership Totals Per Borough', barmode='group')

        dffmap = dfbusdata.copy()
        dffmap = dffmap[dffmap["Year"] == 2020]

        fig6 = px.choropleth_mapbox(dffmap, geojson=counties, locations=locs, color = 'Ridership',
                           color_continuous_scale="Viridis",
                           range_color=(0, 300000000),
                           mapbox_style="carto-positron",
                           zoom=9.2, center = {"lat": 40.7110, "lon": -73.9060},
                           opacity=0.5
                           #labels={'':'Positive Cases'}
                          )
        fig6.update_layout(
            title='2020 Bus Ridership Map')

        dffmap2 = dfbusdata.copy()
        dffmap2 = dffmap2[dffmap2["Year"] == 2019]
        fig7 = px.choropleth_mapbox(dffmap2, geojson=counties, locations=locs, color = 'Ridership',
                           color_continuous_scale="Viridis",
                           range_color=(0, 300000000),
                           mapbox_style="carto-positron",
                           zoom=9.2, center = {"lat": 40.7110, "lon": -73.9060},
                           opacity=0.5
                           #labels={'':'Positive Cases'}
                          )      
        fig7.update_layout(
            title='2019 Bus Ridership Map')            

    if 'bike_button' in changed_id:
        fig5 = px.line(years_dataframe, 
                x="Time", y="Average", color = "Year", title="Bike Count in NYC from 2017-2021")

        fig6 = px.histogram(years_dataframe, 
                x="Time", y="Average", color = "Year", title="Monthly Bike Count from 2019 to 2021", barmode="group")

        fig7 =  px.histogram(bike_data, 
                x="Year", y="Year Average", color="Borough", title="Bike Count by Borough", barmode="group").update_xaxes(categoryorder='total descending')

    if 'car_button' in changed_id:
        fig5=px.line(df_2019
            ,x = 'Month'
            ,y = 'Trips Per Month'
            ,color = 'License Class',
            title="Private Ridership For 2019"
            )
        fig6 = px.scatter(df_2020, x="Month", 
                y="Trips Per Month", color="License Class", 
                title="Private Ridership For 2020")
        fig7 = px.bar(df_2021, x="Month", 
                y="Trips Per Month", color="License Class", title="Private Ridership For 2021")

    return fig5, fig6, fig7



if __name__ == '__main__':
    app.run_server(debug=True)