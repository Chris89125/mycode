#!/usr/bin/python3

"""Flask Driver for game website"""
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for 


"""Flask Constructor"""
app = Flask(__name__)

"""website routes"""
@app.route("/")
def deafult_route():
    return "Welcome to Mad Libs"

@app.route("/ml_start_pg", methods=["GET","POST"])
def ml_start_pg():
    Verb1="running"
    Verb2="swim"
    if request.method == "POST":
        if request.form.get("V1"):
            Verb1 = request.form.get("V1")
            print(Verb1)

        if request.form.get("V2"):
            Verb2 = request.form.get("V2")
            print(Verb2)


    return redirect(url_for("ml_result_pg", V1 = Verb1, V2 = Verb2))
    #return redirect(url_for("app.route", V1 = Verb1, V2 = Verb2))



@app.route("/ml_result_pg/<V1>/<V2>")
def ml_result_pg(V1,V2):
   #  return render_template("ml_start_pg",V1,V2)
   #  return render_template("ml_result_pg.html")
     return render_template("ml_start_pg.html")

@app.route("/about")
def about_route():
    return "<h1>Mad Libs Instructions</h1>"

if __name__ == "__main__":
     #app.run(host="0.0.0.0", port=2224)
     app.run(host="0.0.0.0", port=2224, debug=True)
