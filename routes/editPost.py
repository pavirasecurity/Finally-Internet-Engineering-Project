from helpers import (
    session,
    sqlite3,
    request,
    flash,
    redirect,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    createPostForm,
)

from models import User, Post, Comment, db


editPostBlueprint = Blueprint("editPost", __name__)

@editPostBlueprint.route("/editpost/<int:postID>", methods=["GET", "POST"])
def editPost(postID):
    if "userName" in session:
        post = Post.query.get(postID)

        if post:
            if post.author == session["userName"]:
                form = CreatePostForm(request.form)

                if request.method == "POST" and form.validate():
                    postTitle = request.form["postTitle"]
                    postTags = request.form["postTags"]
                    postContent = request.form["postContent"]

                    if not postContent.strip():
                        flash("محتوای پست نمیتونه خالی باشه", "error")
                    else:
                        post.title = postTitle
                        post.tags = postTags
                        post.content = postContent
                        post.lastEditDate = currentDate()
                        post.lastEditTime = currentTime()

                        db.session.commit()

                        flash("پست ادیت شد", "success")
                        return redirect(f"/post/{post.id}")

                form.postTitle.data = post.title
                form.postTags.data = post.tags
                form.postContent.data = post.content

                return render_template("/editPost.html", title=post.title, tags=post.tags, content=post.content, form=form)
            else:
                flash("این پست وجود ندارد", "error")
                return redirect("/")
        else:
            return render_template("404.html")
    else:
        flash("برای ادیت پست نیاز به لاگین دارین", "error")
        return redirect(f"/login/redirect=&editpost&{postID}")