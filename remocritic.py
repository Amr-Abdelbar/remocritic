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

    url = "https://opencritic-api.p.rapidapi.com/game/reviewed-this-week"
    headers = {
	"x-rapidapi-key": "a374990eafmsh0e1261ce05bf6f1p1c7012jsn9edd139d87b7",
	"x-rapidapi-host": "opencritic-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    return render_template("index.html", content = response.json())

@app.route("/searchResults")
def search_results():
    return get_html("searchResults")

@app.route("/browseAll")
def browse_all():
    return get_html("browseAll")

@app.route("/localUserLibrary")
def local_user_lib():
    return get_html("localUserLibrary")

