from helpers import (
    session,
    sqlite3,
    flash,
    redirect,
    render_template,
    Blueprint,
    request,
)
from delete import deletePost

from models import User, Post, Comment, db


dashboardBlueprint = Blueprint("dashboard", __name__)


@dashboardBlueprint.route("/dashboard/<userName>", methods=["GET", "POST"])
def dashboard(userName):
    if "userName" in session:
        if session["userName"].lower() == userName.lower():
            posts = Post.query.filter_by(author=session["userName"]).all()
            comments = Comment.query.filter_by(user=userName.lower()).all()

            if request.method == "POST":
                if "postDeleteButton" in request.form:
                    postID = request.form["postID"]
                    deletePost(postID)
                    return redirect(f"/dashboard/{userName}")

            showPosts = bool(posts)
            showComments = bool(comments)

            return render_template(
                "/dashboard.html",
                posts=posts,
                comments=comments,
                showPosts=showPosts,
                showComments=showComments,
            )
        else:
            return redirect(f'/dashboard/{session["userName"].lower()}')
    else:
        flash("برای دسترسی به داشبورد لاگین کنید", "error")
        return redirect("/login/redirect=&dashboard&user")