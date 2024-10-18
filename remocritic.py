import datetime
import json
import matplotlib as plt
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask("RemoCritic")

def get_html(file_name):
    html_file = open(file_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/", methods = ["GET", "POST"] )
def homepage():
    
    if request.method == 'GET':
        headers = {
        "x-rapidapi-key": "a374990eafmsh0e1261ce05bf6f1p1c7012jsn9edd139d87b7",
        "x-rapidapi-host": "opencritic-api.p.rapidapi.com"
        }

        week_url = "https://opencritic-api.p.rapidapi.com/game/reviewed-this-week"
        upcoming_url = "https://opencritic-api.p.rapidapi.com/game/upcoming"
        popular_url = "https://opencritic-api.p.rapidapi.com/game/popular"

        popular_response = requests.get(popular_url, headers=headers).json()
        week_response = requests.get(week_url, headers=headers).json()
        upcoming_response = requests.get(upcoming_url, headers=headers).json()

        if (len(week_response) < len(upcoming_response)):
            popular_response = popular_response[:len(week_response)]        
            upcoming_response = upcoming_response[:len(week_response)]    
        else:
            popular_response = popular_response[:len(upcoming_response)]        
            week_response = week_response[:len(upcoming_response)]

        return render_template("index.html", this_week = week_response, popular = popular_response, upcoming = upcoming_response)
        
    else:
        search_value = request.form['search']
        querystring = {"criteria":search_value}
        url = "https://opencritic-api.p.rapidapi.com/game/search"
        search_response = requests.get(url, headers=headers, params=querystring).json()
        print(search_response)

        return redirect(url_for('searchResults', search_response=search_response))

@app.route("/searchResults/<result>")
def search_results(result):


    return render_template("searchResults", result=result)

@app.route("/browseAll")
def browse_all():
    return render_template("browseAll")

@app.route("/localUserLibrary")
def local_user_lib():
    return render_template("localUserLibrary")

@app.route("/game")
def game():
     
    url = f"https://opencritic-api.p.rapidapi.com//game/{id}"

    headers = {
	"x-rapidapi-key": "a374990eafmsh0e1261ce05bf6f1p1c7012jsn9edd139d87b7",
	"x-rapidapi-host": "opencritic-api.p.rapidapi.com"
    }

    

     
    return render_template("game.html")

if __name__ == '__main__':
    app.run(debug=True)