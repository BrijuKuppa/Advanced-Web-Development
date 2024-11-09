from flask import *
app=Flask(__name__)

@app.route("/")

def ar():
    return ("""<p>This is some text made in Python using HTML</p>
    <p>Insert '/more' in the url to access more text.""")

@app.route("/more")

def more():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)