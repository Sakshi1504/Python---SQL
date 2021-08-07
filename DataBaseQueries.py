import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", passwd="sakshi")
print("Connection: ", conn)

mycursor=conn.cursor()

#mycursor.execute("Create Database SakshiDB")

mycursor.execute("Show  databases")

for db in mycursor:
    print(db)
