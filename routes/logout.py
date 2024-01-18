from helpers import session, redirect, Blueprint

from models import User, Post, Comment, db



logoutBlueprint = Blueprint("logout", __name__)


@logoutBlueprint.route("/logout")
def logout():
    match "userName" in session:
        case True:
            session.clear()
            return redirect("/")
        case False:
            return redirect("/")
