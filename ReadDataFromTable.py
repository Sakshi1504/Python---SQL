import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", passwd="sakshi", database="sakshidb")

mycursor=con.cursor()

#mycursor.execute("Select name from employee")

#for db in mycursor:
#    print(db)


#data1=mycursor.fetchone()

#for i in data1:
#    print(i)


mycursor.execute("select * from employee")

data2=mycursor.fetchall()

for j in data2:
    print(j)