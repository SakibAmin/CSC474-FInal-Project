import pandas as pd

"""Reads from all Citibike monthly files from 2017-2022 and counts the number of rows to determine how many Trips were taken in that month. These trip counts per month are saved in a dataframe with the columns
Month, Ridership Trip Count, and Year. Then the dataframe is converted to a .csv file named 'CitiBike Trips 2017-2022.csv' to be read in the python file CitiBike_visualization_2017-2022.py to show the line chart
of ridership trips by year over months.

"""
paths_2017 = [

    #files for 2017 could not be added to github due to storage issues therefore they are read locally
    'Datasets\\CitiBike Data\\2017\\201701-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201702-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201703-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201704-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201705-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201706-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201707-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201708-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201709-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201710-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201711-citibike-tripdata.csv', 
    'Datasets\\CitiBike Data\\2017\\201712-citibike-tripdata.csv'
   
]

paths_2018 = [
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201801-citibike-tripdata.csv', #January 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201802-citibike-tripdata.csv', #Feburary 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201803-citibike-tripdata.csv', #March 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201804-citibike-tripdata.csv', #April 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201805-citibike-tripdata.csv', #May 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201806-citibike-tripdata.csv', #June 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201807-citibike-tripdata.csv', #July 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201808-citibike-tripdata.csv', #August 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201809-citibike-tripdata.csv', #September 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201810-citibike-tripdata.csv', #October 2018    
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201811-citibike-tripdata.csv', #November 2018
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2018/JC-201812-citibike-tripdata.csv', #December 2018
]

paths_2019 = [

    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201901-citibike-tripdata.csv', #January 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201902-citibike-tripdata.csv', #Feburary 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201903-citibike-tripdata.csv', #March 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201904-citibike-tripdata.csv', #April 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201905-citibike-tripdata.csv', #May 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201906-citibike-tripdata.csv', #June 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201907-citibike-tripdata.csv', #July 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201908-citibike-tripdata.csv', #August 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201909-citibike-tripdata.csv', #September 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201910-citibike-tripdata.csv', #October 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201911-citibike-tripdata.csv', #November 2019
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2019/JC-201912-citibike-tripdata.csv'  #December 2019

]

paths_2020 = [
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202001-citibike-tripdata.csv', #January 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202002-citibike-tripdata.csv', #Feburary 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202003-citibike-tripdata.csv', #March 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202004-citibike-tripdata.csv', #April 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202005-citibike-tripdata.csv', #May 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202006-citibike-tripdata.csv', #June 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202007-citibike-tripdata.csv', #July 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202008-citibike-tripdata.csv', #August 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202009-citibike-tripdata.csv', #September 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202010-citibike-tripdata.csv', #October 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202011-citibike-tripdata.csv', #November 2020
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2020/JC-202012-citibike-tripdata.csv'  #December 2020

]

paths_2021 = [

    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202101-citibike-tripdata.csv', #January 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202102-citibike-tripdata.csv', #Feburary 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202103-citibike-tripdata.csv', #March 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202104-citibike-tripdata.csv', #April 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202105-citibike-tripdata.csv', #May 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202106-citibike-tripdata.csv', #June 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202107-citibike-tripdata.csv', #July 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202108-citibike-tripdata.csv', #August 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202109-citibike-tripdata.csv', #September 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202110-citibike-tripdata.csv', #October 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202111-citibike-tripdata.csv', #November 2021
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2021/JC-202112-citibike-tripdata.csv'  #December 2021
]


paths_2022 = [

    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2022/JC-202201-citibike-tripdata.csv', #January 2022
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2022/JC-202202-citibike-tripdata.csv', #Feburary 2022
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2022/JC-202203-citibike-tripdata.csv', #March 2022
    'https://raw.githubusercontent.com/SakibAmin/CSC474-FInal-Project/main/Datasets/CitiBike%20Data/2022/JC-202204-citibike-tripdata.csv'  #April 2022
    
]


months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
month2022 = ['January', 'Feburary', 'March', 'April']


"""reads every month-file from a year-list to determine """
def countRecords(paths_by_year, year, months):
    counts = list()
    yearlist = list()
    for i in range(len(paths_by_year)): 
        file_data = pd.read_csv(paths_by_year[i])
        counts.append(len(file_data.index))
        yearlist.append(year)


    frame= pd.DataFrame({'Month': months, 'Ridership Trip Count': counts})
    frame['Year'] =  yearlist

    return frame #returns a list of the counts

frame2017 = countRecords(paths_2017, 2017, months) #dataframe for 2017
frame2018 = countRecords(paths_2018, 2018, months) #dataframe for 2018
frame2019 = countRecords(paths_2019, 2019, months) #dataframe for 2019
frame2020 = countRecords(paths_2020, 2020, months) #dataframe for 2020
frame2021 = countRecords(paths_2021, 2021, months) #dataframe for 2021
frame2022 = countRecords(paths_2022, 2022, month2022)  #dataframe for 2022

allframeslist = [frame2017, frame2018, frame2019, frame2020, frame2021, frame2022] #makes list out of all year dataframes

final_frame = pd.concat(allframeslist)


final_frame.to_csv('CitiBike Trips 2017-2022.csv')

