import mysql.connector

con = mysql.connector.connect(host="bpgfgctbrm9rowvrggxd-mysql.services.clever-cloud.com",
                              user="uwpf2q04p4q5xodv",
                              password="VLoXSieQ0qbxO20LppUm",
                              database="bpgfgctbrm9rowvrggxd")

if con:
    print("Connected to Database")
else:
    print("Unable to connect to Database")

res = con.cursor()

sql_table="CREATE TABLE IF NOT EXISTS Employee (ID VARCHAR(255), Name VARCHAR(255), Place VARCHAR(255), Age VARCHAR(255))"
sql_table_data="INSERT INTO Employee (ID, Name, Place, Age) VALUES ('1','Lim','Malaysia','10'), ('2','Caryn','UAE','11')"
sql_alter_name="ALTER TABLE Employee RENAME TO Students"
sql_add_column="ALTER TABLE Students ADD Grade VARCHAR(255)"
sql_insert_data_column="INSERT INTO Students (Grade) VALUES ('7'), ('8')"

res.execute(sql_table)
print("Table created")
res.execute(sql_table_data)
print("Table info inserted")

change=input("Do you want to change the table name from 'Employee' to 'Students', add a column with the name 'Grade', and add info to the new column? (Type 'yes' or 'no'):")
if change=="yes":
    res.execute(sql_alter_name)
    print("Table name changed")
    res.execute(sql_add_column)
    print("Added column to table")
    res.execute(sql_insert_data_column)
    print("Added data to new column")
else:
    print("Table name not changed.")







con.commit()