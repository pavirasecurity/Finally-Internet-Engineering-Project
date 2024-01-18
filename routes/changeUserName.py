from helpers import (
    session,
    sqlite3,
    request,
    flash,
    redirect,
    render_template,
    Blueprint,
    changeUserNameForm,
)

from models import User, Post, Comment, db


changeUserNameBlueprint = Blueprint("changeUserName", __name__)


@changeUserNameBlueprint.route("/changeusername", methods=["GET", "POST"])
def changeUserName():
    if "userName" in session:
        form = ChangeUserNameForm(request.form)

        if request.method == "POST" and form.validate():
            newUserName = request.form["newUserName"]
            newUserName = newUserName.replace(" ", "")

            user_check = User.query.filter_by(userName=newUserName).first()

            if newUserName.isascii():
                if newUserName == session["userName"]:
                    flash("یوزرنیم شما همین می باشد", "error")
                elif not user_check:
                    user = User.query.filter_by(userName=session["userName"]).first()
                    user.userName = newUserName
                    db.session.commit()

                    post_updates = Post.query.filter_by(author=session["userName"]).update({"author": newUserName})
                    comment_updates = Comment.query.filter_by(user=session["userName"]).update({"user": newUserName})
                    db.session.commit()

                    session["userName"] = newUserName
                    flash("یوزرنیم عوض شد", "success")
                    return redirect(f"/user/{newUserName.lower()}")
                else:
                    flash("این یوزرنیم از قبل وجود دارد", "error")
            else:
                flash("فرمت یوزرنیم مشکل دارد", "error")

        return render_template("changeUserName.html", form=form)
    else:
        return redirect("/")