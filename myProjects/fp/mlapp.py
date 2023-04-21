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
@app.route("/ml_start_pg")
def ml_result_pg_dsp():
     return render_template("ml_start_pg.html")

"""Render results page. If the user did not enter a variable it will"""
@app.route("/ml_result_pg/results",methods=["GET","POST"])
def ml_result_pg():
    verb1="VERB1"
    verb2="VERB2"
    adverb1="ADVERB1"
    noun1="NOUN1"

    """Capture user input and turns it into a variable
        If the user did not enter a variable 
        it will have a deafult value which are listed above"""
    if request.method == "POST":
        if request.form.get("v1"):
            verb1 = request.form.get("v1") 

        if request.form.get("v2"):
            verb2 = request.form.get("v2")
        
        if request.form.get("adv1"):
            adverb1 = request.form.get("adv1")
            
        if request.form.get("n1"):
            noun1 = request.form.get("n1")

    return render_template("ml_result_pg.html",v1=verb1,v2=verb2,adv1=adverb1,n1=noun1)


"""Render the about page"""
@app.route("/about")
def about_route():
    return "<h1>Mad Libs Instructions</h1>"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=2224)
     #app.run(host="0.0.0.0", port=2224, debug=True)
