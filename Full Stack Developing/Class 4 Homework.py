import random

from flask import *
import random
app=Flask("__name__")

num=random.randint(1,100)


@app.route("/")
@app.route("/guess")
def render_func():
    return render_template("guess.html")
@app.route("/guess",methods=['GET','POST'])
def result():
    if request.method=="POST":
        guess=int(request.form.get("guess"))

        if guess > num:
            message="Your number is to high!"

        elif guess < num:
            message="Your number is to low!"

        elif guess == num:
            message="You guess the correct number! Congrats!"


        return render_template("guess.html",message=message)



if __name__=="__main__":
    app.run(debug=True)