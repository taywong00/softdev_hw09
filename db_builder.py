import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#TASK:
# 1. create a new SQLite database
# 2. utilize csv.DictReader() to read each provided CSV file
# 3. create a table for each
# 4. populate each table

#command = ""          #put SQL statement in this string
#c.execute(command)    #run SQL statement


#open csv files
courses = csv.DictReader(open("courses.csv"))
students = csv.DictReader(open("peeps.csv"))

#==========TEMPLATES===============
#create table template
create_table_temp = "CREATE TABLE table_name (columns_TYPES)"
table_name = ""
columns_TYPES = ""

#insert into template
vals = ""
insert_into_temp = "INSERT INTO table_name VALUES" #(values, ...)

#=============COURSES======================
#create courses table (replacing temp vars)
table_name = "Courses"
columns_TYPES = "code TEXT, mark NUMERIC, id NUMERIC"
create_table = create_table_temp.replace("table_name", table_name)
create_table = create_table.replace("columns_TYPES", columns_TYPES)

try:
    c.execute(create_table)
except:
    print table_name + " TABLE ALREADY EXISTS!!!!!!!!"

#fill out courses table
insert_into = insert_into_temp.replace("table_name", table_name)
#insert_into = insert_into.replace("fields", "code, mark, id")

for row in courses:
    vals = "(\'" + row["code"] + "\', " + row["mark"] + ", " + row["id"] + ")"
    #print vals
    #insert_into = insert_into.replace("vals", vals)
    print insert_into
    print vals
    c.execute(insert_into + vals)

#============STUDENTS=============================
#create students table (replacing temp vars)
table_name = "Students"
columns_TYPES = "name TEXT, age NUMERIC, id NUMERIC"
create_table = create_table_temp.replace("table_name", table_name)
create_table = create_table.replace("columns_TYPES", columns_TYPES)

try:
    c.execute(create_table)
except:
    print table_name + " TABLE ALREADY EXISTS!!!!!!!!"

#fill out courses table
insert_into = insert_into_temp.replace("table_name", table_name)
#insert_into = insert_into.replace("fields", "code, mark, id")

for row in students:
    vals = "(\'" + row["name"] + "\', " + row["age"] + ", " + row["id"] + ")"
    #print vals
    #insert_into = insert_into.replace("vals", vals)
    print insert_into
    print vals
    c.execute(insert_into + vals)


#==========================================================
db.commit() #save changes
db.close()  #close database
