#import libraries
import pandas as pd
import sql
import mysql.connector
from pandas.io import sql

#read from ActiGraph Data
df = pd.read_csv('/Users/Beach/PycharmProjects/pandaspractive/P25-Actigraph.csv', names = ['Time','XAxis','YAxis','ZAxis'])

#Print Sample
print(df.head())

#connect to database
cnx = mysql.connector.connect(user='root', password=yourpasswordhere,
                              host='localhost',
                              database='pandasfun')

cursor = cnx.cursor()

#write to table in database
sql.write_frame(df, con=cnx, name='Actigraph',
                if_exists='replace', flavor='mysql')



#close connection
cursor.close()
cnx.close()