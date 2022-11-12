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


#Querry1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
#Querry2 = "CREATE TABLE Scores (userid int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
#mycursor.execute(Querry1)
#mycursor.execute(Querry2)
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
   #print(x)
   
#users =[("Ludwik", "Ludwik123"),
    #("Diana", "MarynarzTeam"),
    #("Leon", "Leo"),
    #("Dalia", "Flower")]

#user_scores =[(40,100), (20,200), (40,120), (10,20)]
    
#mycursor.executemany("INSERT INTO Users (name, passwd) VALUES (%s, %s)", users)
#Querry3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"
#Querry4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s,%s,%s)"
#for x, user in enumerate(users):
    #mycursor.execute(Querry3, user)
    #last_id = mycursor.lastrowid
    #mycursor.execute(Querry4,(last_id,) + user_scores[x])
#db.commit()

#mycursor.execute("SELECT COLUMN_NAME from information_schema.columns")
mycursor.execute("SELECT * FROM USERS")
for x in mycursor:
    print(x)

