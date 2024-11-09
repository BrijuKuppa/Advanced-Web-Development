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

# SQL Code
table = "CREATE TABLE IF NOT EXISTS User_Info (UserID VARCHAR(255), Username VARCHAR(255), Password VARCHAR(255))"
ins_table = "INSERT INTO User_Info (UserID, Username, Password) VALUES ('432yu7', 'Sharon@e322', 'mnjd83osiUA'), ('nh10s6', 'Karyn@nmjas6', 'kms73Udn')"
# change_name = "ALTER TABLE User_Info RENAME TO Renamed_User_Info"
# add_column = "ALTER TABLE User_Info ADD Email VARCHAR(255)"
select = "SELECT * FROM User_Info"

# Executing SQL
res.execute(table)
print("Table Synthesized")
res.execute(ins_table)
print("Table Values Updated")
# res.execute(change_name)
# print("Table Name Altered")
# res.execute(add_column)
# print("New Column Synthesized")
res.execute(select)
data = res.fetchall()
print(data)
print("Table Has Been Fetched And Printed (As Shown Above)")

for i in data:
    print(i[1])
con.commit()