from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)

from models import User, Post, Comment, db


searchBlueprint = Blueprint("search", __name__)


@searchBlueprint.route("/search/<query>", methods=["GET", "POST"])
def search(query):
    queryNoWhiteSpace = query.replace("+", "")
    query = query.replace("+", " ")

    queryUsers = User.query.filter(User.userName.like(f"%{query}%")).all()
    queryUsersNoWhiteSpace = User.query.filter(User.userName.like(f"%{queryNoWhiteSpace}%")).all()

    queryTags = Post.query.filter(Post.tags.like(f"%{query}%")).all()
    queryTitles = Post.query.filter(Post.title.like(f"%{query}%")).all()
    queryAuthors = Post.query.filter(Post.author.like(f"%{query}%")).all()

    queryTagsNoWhiteSpace = Post.query.filter(Post.tags.like(f"%{queryNoWhiteSpace}%")).all()
    queryTitlesNoWhiteSpace = Post.query.filter(Post.title.like(f"%{queryNoWhiteSpace}%")).all()
    queryAuthorsNoWhiteSpace = Post.query.filter(Post.author.like(f"%{queryNoWhiteSpace}%")).all()

    posts = []
    users = []
    empty = False

    if queryTags:
        posts.append(queryTags)
    if queryTitles:
        posts.append(queryTitles)
    if queryAuthors:
        posts.append(queryAuthors)

    if queryTagsNoWhiteSpace:
        posts.append(queryTagsNoWhiteSpace)
    if queryTitlesNoWhiteSpace:
        posts.append(queryTitlesNoWhiteSpace)
    if queryAuthorsNoWhiteSpace:
        posts.append(queryAuthorsNoWhiteSpace)

    resultsID = list(set(post.id for post in [item for sublist in posts for item in sublist]))
    posts = Post.query.filter(Post.id.in_(resultsID)).all()

    if queryUsers:
        users.append(queryUsers)
    if queryUsersNoWhiteSpace:
        users.append(queryUsersNoWhiteSpace)

    if not posts and not users:
        empty = True

    return render_template(
        "search.html",
        posts=posts,
        users=users,
        query=query,
        empty=empty,
    )