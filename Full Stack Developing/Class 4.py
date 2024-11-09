from flask import *
app=Flask("__name__")

@app.route("/")
def func():
    return render_template("bmi.html")

@app.route("/",methods=["POST","GET"])
def func2():
    if request.method=="POST":
        h=float(request.form.get("ho"))
        w=float(request.form.get("wo"))
        bmi=w/h**2
        bmi=round(bmi,2)
        return render_template("bmi.html",out=bmi)




if __name__ == "__main__":
    app.run(debug=True)