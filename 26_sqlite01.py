import sqlite3
import pandas

# 1 a 2 b 3c


# DBMS ms access, MS SQL Server, MySQL, Oracle, sqlite, mongoDB
# connect -> execute -> commit
# connect()

myConnection = sqlite3.connect("myDatabase.db")

# myCursor = myConnection.execute("create table Students (id INTEGER PRIMARY KEY AUTOINCREMENT, FullName text, Age integer, Address text )") # sql structured query language

# fullName = "Fatema Ashraf"
# age = 23
# address = "Aswan"
# myCursor = myConnection.execute(f"insert into Students (FullName, age, Address) values (?, ?, ?) ", ( fullName, age, address))

# myCursor = myConnection.execute("update students set age = 29 where id = 0 ")
myCursor = myConnection.execute("delete from students where id = 2 ")
myCursor = myConnection.execute("select * from Students where age > 20 order by age ")
allStudents = myCursor.fetchall()
print(allStudents)

myConnection.commit()


