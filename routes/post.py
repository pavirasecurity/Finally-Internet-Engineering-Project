from helpers import (
    session,
    sqlite3,
    request,
    flash,
    redirect,
    addPoints,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    commentForm,
)
from delete import deleteComment, deletePost

from models import User, Post, Comment, db


postBlueprint = Blueprint("post", __name__)


@postBlueprint.route("/post/<int:postID>", methods=["GET", "POST"])
def post(postID):
    form = CommentForm(request.form)

    if request.method == "POST" and form.validate():
        if "userName" in session:
            post = Post.query.get(postID)
            if post:
                if "postDeleteButton" in request.form:
                    deletePost(postID)
                    return redirect("/")
                elif "commentDeleteButton" in request.form:
                    deleteComment(request.form["commentID"])
                    return redirect(f"/post/{postID}")
                else:
                    comment = request.form["comment"]
                    new_comment = Comment(
                        post=postID,
                        comment=comment,
                        user=session["userName"],
                        date=currentDate(),
                        time=currentTime(),
                    )

                    db.session.add(new_comment)
                    db.session.commit()

                    addPoints(5, session["userName"])
                    flash("برای کامنت ۵ امتیاز گرفتی هورا", "success")
                    return redirect(f"/post/{postID}")
            else:
                return render_template("404.html")
        else:
            flash("برای کامنت جدید لاگین کنید", "error")
            return redirect(f"/login/redirect=&post&{postID}")

    elif request.method == "GET":
        post = Post.query.get(postID)

        if post:
            comments = Comment.query.filter_by(post=postID).all()

            return render_template(
                "post.html",
                id=post.id,
                title=post.title,
                tags=post.tags,
                content=post.content,
                author=post.author,
                views=post.views,
                date=post.date,
                time=post.time,
                form=form,
                comments=comments,
            )
        else:
            return render_template("404.html")