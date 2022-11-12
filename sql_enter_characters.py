import mysql.connector
from datetime import datetime
import WTcredentials

db = mysql.connector.connect(
    host = WTcredentials.host,
    user = WTcredentials.user,
    passwd = WTcredentials.passwd,
    database= WTcredentials.database)

mycursor = db.cursor()

sql_query = "INSERT INTO mapping_to_type VALUES (%s, %s)"
sql_values = [
    (0, 'NULL'),

]

mycursor.executemany(sql_query, sql_values)
db.commit()
print(mycursor.rowcount, "was inserted.")