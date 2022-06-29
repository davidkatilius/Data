#This program uses the melt function in Pandas to convert data from wide to long format, and then exports by creating a new CSV.

import csv
import pandas as pd


filename = 'C:\\Users\katil\\Downloads\\SouthDataLong.csv'
csv_file = 'C:\\Users\katil\\Downloads\\SouthCleaned.csv'

#Reading CSV into data frame
df = pd.read_csv(csv_file)

csv_reader = csv.reader(csv_file, delimiter=',')

#Original dataset contained 25 columns of state names. The melt function consolidates those all into one column.
df = df.melt(id_vars =['RespondentID','Southern Identity','Zip Code','Resident State','Gender',
                       'Age','Income','Education','Region'])

#Removing null values, and other clean up
df = df.dropna(subset='value')
df.rename(columns = {'variable':'Southern State'}, inplace = True)
df = df.drop(['value'], axis = 1)
df = df.sort_values('RespondentID',ascending=True)


#Creating new CSV using updated dataframe
df.to_csv(filename, mode='w',index=False)
