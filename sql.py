import sqlite3

connection=sqlite3.connect("student.db")

cursor = connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""



cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',95)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',99)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',92)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',90)''') 

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  

connection.commit() 
  
# Closing the connection 
connection.close()