from flask import *
app=Flask("__name__")
details=[]

@app.route("/")
def rd():
    return render_template("hw3.html")

@app.route("/signups",methods=["POST","GET"])
def sd():
    if request.method=="POST":
        n=request.form.get("name")
        e=request.form.get("email")
        p=request.form.get("phone")
        details.append({"name":n,"email":e,"phone":p})
        return render_template("signups.html",de=details)



if __name__ == "__main__":
    app.run(debug=True)