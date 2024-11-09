from flask import *

app=Flask("__name__")

books=[
    {"image":"https://m.media-amazon.com/images/I/91IAaf98qqL._AC_UF1000,1000_QL80_.jpg",
    "title":"Wings of Fire",
    "author":"Tu T. Sutherland"},

    {"image":"https://m.media-amazon.com/images/I/7167GDebbRL._AC_UF1000,1000_QL80_.jpg",
    "title":"Harry Potter",
    "author":"J.K Roweling"}
    ]

@app.route("/")
def display():
   return render_template("hw2.html", details=books)


if __name__=="__main__":
    app.run(debug=True)