import flask
import os
import requests
import json

app = flask.Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def artist_info(): 
    # return flask.render_template("index.html", test ="hello from template")
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    headers = {
        'x-rapidapi-key': "4d9b84ebc6mshed63a9b2ac6528dp10f43ajsn35c31f287d81",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)

    quotes = (data["content"])
 
    return flask.render_template("index.html", quote=quotes)

# @app.route('/next')
# def quotes():
   


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)