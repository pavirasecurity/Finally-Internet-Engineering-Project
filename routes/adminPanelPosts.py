from helpers import (
    sqlite3,
    render_template,
    Blueprint,
    session,
    redirect,
    request,
)
from delete import deletePost

from models import User, Post, Comment, db


adminPanelPostsBlueprint = Blueprint("adminPanelPosts", __name__)


@adminPanelPostsBlueprint.route("/admin/posts", methods=["GET", "POST"])
@adminPanelPostsBlueprint.route("/adminpanel/posts", methods=["GET", "POST"])
def adminPanelPosts():
    if "userName" in session:
        user = User.query.filter_by(userName=session["userName"]).first()

        if not user:
            return redirect("/")

        if request.method == "POST":
            if "postDeleteButton" in request.form:
                deletePost(request.form["postID"]) 

        if user.role == "admin":
            posts = Post.query.all()
            return render_template("dashboard.html", posts=posts, showPosts=True)
        else:
            return redirect("/")
    else:
        return redirect("/")