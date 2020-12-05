import flask
import os

app = flask.Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def artist_info(): 
    return flask.render_template("index.html", test ="hello from template")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)