from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import json

class Game:
    def __init__(self, name, id, owned = False, beaten = False):
        self.name = name
        self.id = id
        self.owned = owned
        self.beaten = beaten
    
    def add(self):
        self.owned = True

    def remove(self):
        self.owned = False

    def beat(self):
        self.beaten = True

app = Flask("RemoCritic")
app.secret_key = "ua6.czP7*~KSX_4#ym[U"

@app.route("/", methods = ["GET", "POST"] )
def homepage():

    headers = {
        "x-rapidapi-key": "27b4fc4979mshbfd3db75c68c1eap1d626fjsnfa5a4fd9e706",
        "x-rapidapi-host": "opencritic-api.p.rapidapi.com"
        }
    
    if request.method == 'GET':

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
        session['search_results'] = search_response

        return redirect(url_for('search_results'))

@app.route('/userLibrary', methods=['GET', 'POST', 'DELETE'])
def userLibrary():
    if request.method == 'POST':
        data = request.get_json()
        with open("localLib.JSON", "r") as local_lib:
            try:
                lib = json.load(local_lib)
                if data not in lib:
                    lib.append(data)
            except: 
                lib = []
                lib.append(data)
        with open("localLib.JSON", "w") as local_lib:
            json.dump(lib, local_lib)
        
        return jsonify({
            "message": "Stored in game library successfuly",
            "status": 200
        })
    elif request.method == 'GET':
        with open("localLib.JSON", "r") as local_lib:
            lib = json.load(local_lib)

            return render_template("userLibrary.html", userLibrary = lib)
    else:

        data = request.get_json()
        game_id = data.get("id")
        with open("localLib.JSON", "r") as local_lib:
            lib = json.load(local_lib)
        for game in lib:
            if game["id"] == game_id:
                lib.remove(game)
                break

        with open("localLib.JSON", "w") as local_lib:
            json.dump(lib, local_lib)
        
        return jsonify ({
            "message": "Game removed from library",
            "status": 200
        })

@app.route("/searchResults")
def search_results():
    search_response = session.get("search_results", [])

    return render_template("searchResults.html", result = search_response)

@app.route("/game/<id>")
def game(id):

    headers = {
	"x-rapidapi-key": "27b4fc4979mshbfd3db75c68c1eap1d626fjsnfa5a4fd9e706",
	"x-rapidapi-host": "opencritic-api.p.rapidapi.com"
    }

    review_url = f"https://opencritic-api.p.rapidapi.com/reviews/game/{id}"
    review_querystring = {"skip":"20","sort":"newest"}    
    review_response = requests.get(review_url, headers=headers, params = review_querystring).json() 
    game_url = f"https://opencritic-api.p.rapidapi.com/game/{id}"
    game_response = requests.get(game_url, headers = headers).json()

    return render_template("game.html", game = game_response, review=review_response)

if __name__ == '__main__':
    app.run(debug=True)