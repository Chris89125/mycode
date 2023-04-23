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

    adjective1="ADJ1"
    noun1="NOUN1"
    noun2="NOUN2"
    verb1="VERB1"
    liquid1="LIQUID1"
    liquid2="LIQUID2"
    liquid3="LIQUID3"
    color1="COLOR1"
    verb2="VERB2"
    verb3="VERB3"
    number1="NUMBER1"
    adjective2="ADJ2"
    adverb1="ADVERB1"
    body1="BODY1"
    verb4="VERB4"
    verb5="VERB5"


    """Capture user input and turns it into a variable
        If the user did not enter a variable 
        it will have a deafult value which are listed above"""
    if request.method == "POST":
        if request.form.get("adj1"):
            adjective1 = request.form.get("adj1") 

        if request.form.get("n1"):
            noun1 = request.form.get("n1")

        if request.form.get("n2"):
            noun2 = request.form.get("n2")
        
        if request.form.get("v1"):
            verb1 = request.form.get("v1")
        
        if request.form.get("liq1"):
            liquid1 = request.form.get("liq1")

        if request.form.get("liq2"):
            liquid2 = request.form.get("liq2")

        if request.form.get("liq3"):
            liquid3 = request.form.get("liq3")

        if request.form.get("col1"):
            color1 = request.form.get("col1")

        if request.form.get("v2"):
            verb2 = request.form.get("v2")       

        if request.form.get("v3"):
            verb3 = request.form.get("v3")

        if request.form.get("num1"):
            number1 = request.form.get("num1")

        if request.form.get("adj2"):
            adjective2 = request.form.get("adj2")

        if request.form.get("adv1"):
            adverb1 = request.form.get("adv1")

        if request.form.get("bod1"):
            body1 = request.form.get("bod1")

        if request.form.get("v4"):
            verb4 = request.form.get("v4")

        if request.form.get("v5"):
            verb5 = request.form.get("v5")

    return render_template("ml_result_pg.html",adj1=adjective1, n1=noun1, n2=noun2,v1=verb1, liq1=liquid1, liq2=liquid2, liq3=liquid3,col1=color1, v2=verb2, v3=verb3, num1=number1,adj2=adjective2, adv1=adverb1, bod1=body1,v4=verb4, v5=verb5)


"""Render the about page"""
@app.route("/about")
def about_route():
     return render_template("ml_about_pg.html")

if __name__ == "__main__":
     #app.run(host="0.0.0.0", port=2225)
     app.run(host="0.0.0.0", port=2225, debug=True)
