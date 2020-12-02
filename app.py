import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bsom.objectid import ObjectId
if os.path.exists("env.py"):
    import env


    app= Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo= PyMongo(app)

    @app.route("/")
    @app.route("/Anime_list")
    def Anime_list():
        Anime = mongo.db.Anime.find()
        return render_template("AnimeList.html", Anime=Anime)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)