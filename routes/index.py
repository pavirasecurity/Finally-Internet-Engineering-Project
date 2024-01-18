from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)

from models import User, Post, Comment, db

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    db.create_all()
    posts = Post.query.all()
    return render_template(
        "index.html",
        posts=posts,
    )
