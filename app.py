import flask
import os
import requests
import json
import random

app = flask.Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def artist_info(): 
    # return flask.render_template("index.html", test ="hello from template")
    url_2 = "https://quotes15.p.rapidapi.com/quotes/random/"
    headers = {
        'x-rapidapi-key': "4d9b84ebc6mshed63a9b2ac6528dp10f43ajsn35c31f287d81",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
        }

    response = requests.request("GET", url_2, headers=headers)
    data = json.loads(response.text)

    quotes = (data["content"])
    url = "https://api.genius.com/search?q=Pharrell%20Williams"
    # genius_key = os.getenv("GeniusKey")
    genius_key = "t6wt_hu0VvrNOvL6JBhWJAnu7cpB_3cnk6xYegOFWS3dg46qM6Z0MIdu81iq_oOR"
    my_headers = {
        "Authorization": "Bearer  " + genius_key
    }
    response = requests.get(url, headers=my_headers)
    json_body = response.json() 
    
    array = json_body["response"]["hits"]
    r = random.randint(0, len(array) - 1) 
    
    #This gets the id of the song that's playing
    song_id = array[r]["result"]["id"]



    song_link = get_songPlaying(song_id)
    return flask.render_template("index.html", quote = quotes, video = song_link)

def get_songPlaying(song_id):
    song_id_url= "https://api.genius.com/songs/" + str(song_id)
    song_id_genius_key = "sZD99vUmHfcsYnAwtmTIBWsDgTJZjO8qAdzKk5JgGxeMdM4gsktvql3il_0kw0-D"
    # song_id_genius_key = os.getenv("SongIDKey")
    song_id_headers = {
            "Authorization": "Bearer  " + song_id_genius_key
    }
    response2 = requests.get(song_id_url, headers=song_id_headers)
    json_body2 = response2.json()
    
   
    song_link = json_body2["response"]["song"]["apple_music_player_url"]
    return song_link

# @app.route('/next')
# def quotes():
   


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)