from flask_dance.contrib.google import make_google_blueprint, google
from flask import Flask, redirect, url_for
from models import User, Post, Comment, db


blueprint = make_google_blueprint(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login_google")

loginGoogleBlueprint = Blueprint("login_google", __name__)

@loginGoogleBlueprint.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["emails"][0]["value"])