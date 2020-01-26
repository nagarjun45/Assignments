import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="arjun123",
  database="sakila"
)

mycursor = mydb.cursor()
mycursor.execute("create table customers5 (id int,name varchar(20),address varchar(20))")

sql = "INSERT INTO customers5 (id,name, address) VALUES (%s,%s, %s)"
val = (5,"John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
def fetch():
    cursor.execute("select * from tablename")
    for row in cursor.fetchall():
        yield row
print(list(fetch()))
