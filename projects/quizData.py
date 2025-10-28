# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:46:21 2025

@author: Kai
"""
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def cheese():
    return render_template("/survey.html")

@app.route("/",methods = ["POST"])
def happy():
    q1Ans = request.form.get("coolWeather")
    q2Ans = request.form.get("peopleWeather")
    q3Ans = request.form.get("favGraph")
    q4Ans = request.form.get("joke")
    print(q1Ans, q2Ans, q3Ans, q4Ans)
    file = open("answers.csv", "a", newline="")
    pen = csv.writer(file)
    pen.writerow([q1Ans, q2Ans, q3Ans, q4Ans])
    file.close()
    return render_template("/survey.html")
