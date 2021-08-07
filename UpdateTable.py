import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", passwd="sakshi", database="sakshidb")

mycursor=conn.cursor()

name=input("Enter name")

sqlquery="Update employee set id=23 where name='"+name+"'"

#mycursor.execute(sqlquery)

#conn.commit()

mycursor.execute("Select * from employee")

for i in mycursor:
    print(i)