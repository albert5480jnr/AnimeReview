import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


    app= Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
from werkzeug.security import generate_password_hash, check_password_hash
mongo = PyMongo(app)

@app.route("/")
@app.route("/Anime_list ")
def get_Anime_list():
    Anime = mongo.db.tasks.find()
    return render_template("AnimeList.html", Anime=Anime)

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


    if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)