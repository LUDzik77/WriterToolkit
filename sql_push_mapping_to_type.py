import mysql.connector
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
    (1,'ENCOUNTER'),
    (2,'ROMANTIC'),
    (3,'BATTLE'),
    (4,'FRIENDLY'),
    (5,'HOSTILE'),
    (10,'HEROJOURNEY'),
    (11,'INFODUMP'),
    (20,'ITEM'),
    (30,'JOIN'),
    (31,'LEAVE'),
    (50,'INTRO'),
    (51,'BUILDUP'),
    (52,'TWIST'),
    (55,'CONSUMMATION'),
    (56,'AFTERMATH'),
    (12,'MYSTERY'),
    (33,'LEADER'),
    (34,'ABDICATE')
]

mycursor.executemany(sql_query, sql_values)
db.commit()
print(mycursor.rowcount, "was inserted.")







for i in mycursor:
    print(i)

db.commit()