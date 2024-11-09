import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="bpgfgctbrm9rowvrggxd-mysql.services.clever-cloud.com",
                               user="uwpf2q04p4q5xodv",
                               password="VLoXSieQ0qbxO20LppUm",
                               database="bpgfgctbrm9rowvrggxd")

if con:
    print("Connected to Database")
else:
    print("Unable to connect to Database")

res = con.cursor()

sql_table="CREATE TABLE IF NOT EXISTS IPLtb (Position VARCHAR(255), Team VARCHAR(255), NRR VARCHAR(255))"
sql_table_data="INSERT INTO IPLtb (Position, Team, NRR) VALUES ('1','GT','0.809'), ('2','CSK','0.652'), ('3','LSG','0.284'), ('4','MI','-0.044')"
res.execute(sql_table)
print("IPL table successfully created.")
res.execute(sql_table_data)
print("Table data successfully inserted.")





con.commit()