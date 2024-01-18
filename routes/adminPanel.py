from helpers import sqlite3, render_template, Blueprint, session, redirect

from models import *



adminPanelBlueprint = Blueprint("adminPanel", __name__)

@adminPanelBlueprint.route("/admin")
def adminPanel():
    if "userName" in session:
        user = User.query.filter_by(userName=session["userName"]).first()

        if not user:
            return redirect("/")

        if user.role == "admin":
            return render_template("adminPanel.html")
        else:
            return redirect("/")
    else:
        return redirect("/")