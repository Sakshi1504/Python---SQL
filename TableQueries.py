import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", passwd="sakshi", database="sakshidb")

mycursor=conn.cursor()

#mycursor.execute("create table employee(name nvarchar(50), id int(5))")


mycursor.execute("show tables")

for tb in mycursor:
    print(tb)

insertquery="insert into employee(name, id) values(%s, %s)"

details=[("sakshi", 90000), ("prajakta", 100000000)] #in form of tuples, so that multiple rows can be there

#mycursor.executemany(insertquery, details)

conn.commit()