import pymysql
import requests
from bs4 import BeautifulSoup

url=requests.get("Linke for the website")
soup=BeautifulSoup(url.text,features="html.parser")

l=soup.find_all('h3',{'class':'lister-item-header'})
m_name=[]
for x in l:
    for y in x.find_all('a'):
        m_name.append(y.text)
        
m_rate=[]      
r=soup.find_all('div',{'class':'what to find in the page'})
for x in r:
    for y in x.find_all("span",{'class':'related to the class parameter'}):
        m_rate.append(y.text)
print("Scrapping finished")
mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="arjun123"
)
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS MOVIESDB")
mycursor.execute("CREATE DATABASE DBname")
mydb.close()
print("Database created!!!")

db = pymysql.connect("localhost","root","arjun123","Dbname")
cursor = db.cursor()

cursor.execute("CREATE TABLE tablename (id INT AUTO_INCREMENT PRIMARY KEY, colname VARCHAR(255), colname VARCHAR(255))")

sql = "INSERT INTO tablename (col1,col2) VALUES (%s, %s)"
l=len(m_name)
i=0
while(l!=0):
    val=(m_name[i],m_rate[i])
    cursor.execute(sql, val)
    i=i+1
    l=l-1

db.commit()
print("Data Saved!")

def fetch():
    cursor.execute("select * from tablename")
    for row in cursor.fetchall():
        yield row
print(list(fetch()))