from flask import Flask, render_template, request, url_for, redirect
import redis
import flask

redis=redis.Redis(host='localhost',port=6379)
app = Flask(__name__)
app.config["TOKEN"]="bharathkarkera"
app.secret_key = 'bharathkarkera'

@app.route("/")
def index():
    redis.incr("hits")
    flask.flash(str(int(redis.get("hits")))+"th hit to the site !")
    return render_template("index.html")

@app.route("/thankYouShrini")
def display_fun():
    return render_template("display.html")

#app.run(host="0.0.0.0")
