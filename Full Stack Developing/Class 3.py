from flask import *
app=Flask("__name__")
details=[{"name":"Jhon","og":"90"}]
@app.route("/")
def rd():
    return render_template("index3.html")

@app.route("/mark",methods=["POST","GET"])
def od():
    if request.method=="POST":
        n=request.form.get("name")
        g=request.form.get("grade")
        details.append({"name":n,"grade":g})
    return render_template("mark.html", de=details)

if __name__ == "__main__":
    app.run(debug=True)
