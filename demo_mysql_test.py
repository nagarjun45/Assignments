import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "arjun123",
    database = "sakila"
    )
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("use sakila")
#mycursor.execute("create table arjun (id varchar(10),name varchar(20), course varchar(20))")
#mycursor.execute("insert into arjun (id,name,course) values ('3','abc,'cse')")
#mycursor.execute("create table Rohit (id varchar(10),name varchar(20))")
mycursor.execute("create table barun (name te(20), course varchar(20))")

mycursor.execute("insert into barun (id,name) values (%s,%s)","('5','Naga')")
