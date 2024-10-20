import datetime
import json
import matplotlib as plt
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask("RemoCritic")
app.secret_key = "ua6.czP7*~KSX_4#ym[U"

def get_html(file_name):
    html_file = open(file_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/", methods = ["GET", "POST"] )
def homepage():

    headers = {
        "x-rapidapi-key": "a374990eafmsh0e1261ce05bf6f1p1c7012jsn9edd139d87b7",
        "x-rapidapi-host": "opencritic-api.p.rapidapi.com"
        }
    

    
    if request.method == 'GET':


        week_url = "https://opencritic-api.p.rapidapi.com/game/reviewed-this-week"
        upcoming_url = "https://opencritic-api.p.rapidapi.com/game/upcoming"
        popular_url = "https://opencritic-api.p.rapidapi.com/game/popular"

        popular_response = requests.get(popular_url, headers=headers).json()
        week_response = requests.get(week_url, headers=headers).json()
        upcoming_response = requests.get(upcoming_url, headers=headers).json()


        '''
        for game in week_response:
            images = game['images']
            box = images["box"]
            sm = []
            if 'box' in images.keys():
                if 'sm' in box.keys():
                    sm.append(images["box"]["sm"])
                # sm.append(images['box']['sm'])
            # small_img = box['sm']
            # print(type(images))


            # if small_img:
            #     game_images.append(small_img)
            '''
        if (len(week_response) < len(upcoming_response)):
            popular_response = popular_response[:len(week_response)]        
            upcoming_response = upcoming_response[:len(week_response)]

        else:
            popular_response = popular_response[:len(upcoming_response)]        
            week_response = week_response[:len(upcoming_response)]

        return render_template("index.html", this_week = week_response, popular = popular_response, upcoming = upcoming_response, review = review_response)
        
    else:
        
        search_value = request.form['search']
        querystring = {"criteria":search_value}
        url = "https://opencritic-api.p.rapidapi.com/game/search"
        search_response = requests.get(url, headers=headers, params=querystring).json()
        session['search_results'] = search_response

        return redirect(url_for('search_results'))

@app.route("/searchResults")
def search_results():
    search_response = session.get("search_results", [])

    return render_template("searchResults.html", result = search_response)

@app.route("/browseAll")
def browse_all():
    return render_template("browseAll.html")

@app.route("/localUserLibrary")
def local_user_lib():
    return render_template("localUserLibrary.html")

@app.route("/game/{{id}}")
def game():
     
    review_url = f"https://opencritic-api.p.rapidapi.com/reviews/game/{{id}}"
    review_querystring = {"skip":"20","sort":"newest"}    
    review_response = requests.get(review_url, headers=headers, params = review_querystring).json() 
    game_url = f"https://opencritic-api.p.rapidapi.com/game/{{id}}"

    headers = {
	"x-rapidapi-key": "a374990eafmsh0e1261ce05bf6f1p1c7012jsn9edd139d87b7",
	"x-rapidapi-host": "opencritic-api.p.rapidapi.com"
    }

    return render_template("game.html", game = game_url, review=review_response)

if __name__ == '__main__':
    app.run(debug=True)