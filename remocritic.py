import datetime
import json
import matplotlib as plt
import numpy as np

from flask import Flask, render_template
import requests

app = Flask("RemoCritic")

def get_html(file_name):
    html_file = open(file_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/")
def homepage():
    
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

@app.route("/searchResults")
def search_results():
    return get_html("searchResults")

@app.route("/browseAll")
def browse_all():
    return get_html("browseAll")

@app.route("/localUserLibrary")
def local_user_lib():
    return get_html("localUserLibrary")

if __name__ == '__main__':
    app.run(debug=True)