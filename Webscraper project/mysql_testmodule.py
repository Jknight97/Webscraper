import csv
import mysql.connector
from main import outputEntries
from main import totalPosts
from main import dataSets
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "JKnight",
    database = "scraperdb", autocommit=True
)

mycursor = mydb.cursor()
dataFrame = pd.read_csv(r'C:\\Users\\staya\\AppData\\Roaming\\Python\\Python39\\Python Projects\\Projects\pandas_data.csv')
data_file = open('pandas_data.csv')
csv_data = csv.reader(data_file)

outputEntries(totalPosts)

skipHeader = True

for row in csv_data:
	if skipHeader:
		skipHeader = False
		continue
	mycursor.execute("INSERT INTO parsed_data (elapsedMinutes, postDate, postTitle, postURL) VALUES ('%s', '%s', '%s', '%s')" % ())

query = "LOAD DATA LOCAL INFILE 'C:\\Users\\staya\\AppData\\Roaming\\Coderboy\\Python\\Python39\\Python Projects\\Projects' INTO TABLE parsed_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 LINES (elapsedMinutes, postDate, postTitle, postURL)"

mycursor.execute(query)

mydb.commit()

print(mycursor.rowcount, "record inserted")

for x in mycursor:
    print(x)
