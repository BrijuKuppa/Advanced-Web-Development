import mysql.connector

con = mysql.connector.connect(host="bzvv7y4gwfitdst8f36u-mysql.services.clever-cloud.com",
                              user="umycepmqazozs5um",
                              password="WsDagVuABCIn6K634h3r",
                              database="bzvv7y4gwfitdst8f36u")

if con:
    print("Connected to Database")
else:
    print("Unable to connect to Database")

point = con.cursor()
sql_table = "CREATE TABLE DBTable (Column1 VARCHAR(255), Column2 VARCHAR(255))"
sql_insert = "INSERT INTO DBTable (Column1, Column2) VALUES ('This is some data in Column1','This is some data in Column2')"
# sql_drop = "DROP TABLE DBTable"
data=point.fetchall()
print(data)
# point.execute(sql_table)
# point.execute(sql_insert)
print("Table Synthesized")
con.commit()