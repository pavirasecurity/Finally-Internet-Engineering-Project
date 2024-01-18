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
    createPostForm,
)

from models import User, Post, Comment, db


createPostBlueprint = Blueprint("createPost", __name__)


@createPostBlueprint.route("/createpost", methods=["GET", "POST"])
def createPost():
    if "userName" in session:
        form = CreatePostForm(request.form)

        if request.method == "POST" and form.validate():
            postTitle = request.form["postTitle"]
            postTags = request.form["postTags"]
            postContent = request.form["postContent"]

            if not postContent.strip():
                flash("محتوای پست نمیتونه خالی باشد", "error")
            else:
                post = Post(
                    title=postTitle,
                    tags=postTags,
                    content=postContent,
                    author=session["userName"],
                    views=0,
                    date=currentDate(),
                    time=currentTime(),
                    lastEditDate=currentDate(),
                    lastEditTime=currentTime(),
                )

                db.session.add(post)
                db.session.commit()

                addPoints(20, session["userName"])
                flash("شما برای این پست بیست امتیاز گرفتین", "success")
                return redirect("/")
                
        return render_template("createPost.html", form=form)
    else:
        flash("شما برای ساخت پست نیاز به لاگین دارین", "error")
        return redirect("/login/redirect=&createpost")