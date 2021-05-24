import mysql.connector
from main import *

outputEntries(totalPosts)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "JKnight",
    password = "Coderboygobrrr42069",
    database = "scraperdb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO parsed_data (elapsedMinutes, postDate, postTitle, postURL) VALUES (%i, %s, %s, %s)"

#val = 


mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

for x in mycursor:
    print(x)