import mysql.connector

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
mycursor.execute("SELECT * FROM Person")


for x in mycursor:
    print(x)

