from helpers import (
    sqlite3,
    render_template,
    Blueprint,
    session,
    redirect,
    request,
)
from delete import deleteComment

from models import User, Post, Comment, db


adminPanelCommentsBlueprint = Blueprint("adminPanelComments", __name__)

@adminPanelCommentsBlueprint.route("/admin/comments", methods=["GET", "POST"])
@adminPanelCommentsBlueprint.route("/adminpanel/comments", methods=["GET", "POST"])
def adminPanelComments():
    if "userName" in session:
        user = User.query.filter_by(userName=session["userName"]).first()

        if not user:
            return redirect("/")

        if request.method == "POST":
            if "commentDeleteButton" in request.form:
                deleteComment(request.form["commentID"])
                return redirect("/admin/comments")

        if user.role == "admin":
            comments = Comment.query.all()
            return render_template("adminPanelComments.html", comments=comments)
        else:
            return redirect("/")
    else:
        return redirect("/")