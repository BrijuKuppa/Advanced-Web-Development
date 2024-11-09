from flask import *
import mysql.connector

con = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="registers_infyni")

if con:
    print("Connected to Database")
else:
    print("Unable to connect to Database")

res=con.cursor()
# sql_table="CREATE TABLE IF NOT EXISTS Users (ID INT PRIMARY KEY AUTO_INCREMENT, Email VARCHAR(150) UNIQUE, Username VARCHAR(200), Password VARCHAR(250))"
# res.execute(sql_table)
# print("Table created")


# con.commit()


app=Flask("__name__")
@app.route("/")
@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method=="POST":
        uname=request.form.get("uname")
        email=request.form.get("email")
        password=request.form.get("password")
        sql_email="SELECT * FROM Users WHERE Email = %s"
        res.execute(sql_email,(email,))
        data=res.fetchall()
        if data:
            message="This email is already used. Please use another one."
            return render_template("register.html", message=message)
        else:
            sql_insert = "INSERT INTO Users (Email, Username, Password) VALUES (%s,%s,%s)"
            res.execute(sql_insert, (email, uname, password))
            con.commit()
            return render_template("infyni.html")


    return render_template("register.html",normal=" Email")





@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        passw=request.form.get("passw")
        sql_select="SELECT * FROM Users WHERE Username=%s AND Password=%s"
        res.execute(sql_select, (username, passw))
        data=res.fetchall()
        print(data)
        con.commit()

        if data:
            return render_template("infyni.html")

        else:
            error="One of the fields are not right please try again."
            return render_template("login.html", error=error)

    return render_template("login.html", error="")



if __name__ == "__main__":
    app.run(debug=True)