from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)

from models import User, Post, Comment, db


userBlueprint = Blueprint("user", __name__)


@userBlueprint.route("/user/<userName>")
def user(userName):
    user = User.query.filter_by(userName=userName).first()
    users = User.query.all()

    if any(str(userName).lower() in str(user).lower() for user in users):
        views = 0
        posts = Post.query.filter_by(author=user.userName).all()
        
        for post in posts:
            views += post.views

        comments = Comment.query.filter_by(user=userName.lower()).all()

        showPosts = bool(posts)
        showComments = bool(comments)

        return render_template(
            "user.html",
            user=user,
            views=views,
            posts=posts,
            comments=comments,
            showPosts=showPosts,
            showComments=showComments,
        )

    else:
        return render_template("404.html")