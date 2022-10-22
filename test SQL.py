import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "Ludwik",
    passwd = "Ludwik",
    database= "testdatabase")

mycursor = db.cursor()

#useful mysql related code snippets:
#mycursor.execute("CREATE DATABASE testdatabase")
#mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Karol",36))
#db.commit()

#mycursor.execute("DESCRIBE Person")
#mycursor.execute("SELECT * FROM Person")

#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M','F','O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("TIM", datetime.now(), "M"))
#db.commit()

#mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id DESC")
#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
#mycursor.execute("ALTER TABLE name first_name VARCHAR(50)")
for x in mycursor:
   print(x)

