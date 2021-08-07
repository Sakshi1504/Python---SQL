import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", passwd="sakshi", database="sakshidb")

mycursor=con.cursor()

name=input("Enter Name to be deleted")

delq="delete from employee where name='"+name+"'"

mycursor.execute(delq)

con.commit()