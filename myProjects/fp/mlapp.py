#!/usr/bin/python3

"""Flask Driver for game website"""
from flask import Flask
from flask import render_template



"""Flask Constructor"""
app = Flask(__name__)

"""website routes"""
@app.route("/")
def deafult_route():
    return "Welcome to Mad Libs"

@app.route("/ml_start_pg")
def ml_start_pg():
    return render_template("ml_start_pg.html")

@app.route("/ml_results_pg")
def ml_results_pg():
    return render_template("ml_result_pg.html")

@app.route("/about")
def about_route():
    return "<h1>Mad Libs Instructions</h1>"

if __name__ == "__main__":
     #app.run(host="0.0.0.0", port=2224)
     app.run(host="0.0.0.0", port=2224, debug=True)
