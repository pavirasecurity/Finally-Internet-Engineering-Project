from helpers import (
    sqlite3,
    render_template,
    Blueprint,
    session,
    redirect,
    request,
)
from delete import deleteUser

from models import User, Post, Comment, db


adminPanelUsersBlueprint = Blueprint("adminPanelUsers", __name__)


@adminPanelUsersBlueprint.route("/admin/users", methods=["GET", "POST"])
@adminPanelUsersBlueprint.route("/adminpanel/users", methods=["GET", "POST"])
def adminPanelUsers():
    if "userName" in session:
        user = User.query.filter_by(userName=session["userName"]).first()

        if not user:
            return redirect("/")

        if request.method == "POST":
            if "userDeleteButton" in request.form:
                deleteUser(request.form["userName"]) 

        if user.role == "admin":
            users = User.query.all()
            return render_template("adminPanelUsers.html", users=users)
        else:
            return redirect("/")
    else:
        return redirect("/")