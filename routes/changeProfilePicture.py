from helpers import (
    session,
    sqlite3,
    request,
    flash,
    redirect,
    render_template,
    Blueprint,
    changeProfilePictureForm,
)

from models import User, Post, Comment, db


changeProfilePictureBlueprint = Blueprint("changeProfilePicture", __name__)


@changeProfilePictureBlueprint.route("/changeprofilepicture", methods=["GET", "POST"])
def changeProfilePicture():
    if "userName" in session:
        form = ChangeProfilePictureForm(request.form)

        if request.method == "POST" and form.validate():
            newProfilePictureSeed = request.form["newProfilePictureSeed"]
            newProfilePicture = f"https://api.dicebear.com/7.x/identicon/svg?seed={newProfilePictureSeed}&radius=10"

            user = User.query.filter_by(userName=session["userName"]).first()

            if user:
                user.profilePicture = newProfilePicture
                db.session.commit()

                flash("عکس پروفایل عوض شد", "success")
                return redirect("/changeprofilepicture")

        return render_template("changeProfilePicture.html", form=form)
    else:
        return redirect("/")