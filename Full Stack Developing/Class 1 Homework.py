from flask import *
app=Flask(__name__)

@app.route("/")
def mtext():
    return("This is the main page. Type '/about' in the url for more info.")

@app.route("/about")
def atext():
    return("This is the about page.")

if __name__=="__main__":
    app.run(debug=True)
