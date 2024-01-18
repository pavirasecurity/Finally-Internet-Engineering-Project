from helpers import (
    session,
    sqlite3,
    request,
    flash,
    redirect,
    render_template,
    Blueprint,
    sha256_crypt,
    changePasswordForm,
)

from models import User, Post, Comment, db


changePasswordBlueprint = Blueprint("changePassword", __name__)


@changePasswordBlueprint.route("/changepassword", methods=["GET", "POST"])
def changePassword():
    if "userName" in session:
        form = ChangePasswordForm(request.form)
        
        if request.method == "POST" and form.validate():
            oldPassword = request.form["oldPassword"]
            password = request.form["password"]
            passwordConfirm = request.form["passwordConfirm"]

            user = User.query.filter_by(userName=session["userName"]).first()

            if user and sha256_crypt.verify(oldPassword, user.password):
                if oldPassword == password:
                    flash("پسورد جدید با رمز عبور قدیمی یکسان است", "error")
                elif password != passwordConfirm:
                    flash("پسورد یکسان نیست", "error")
                elif oldPassword != password and password == passwordConfirm:
                    new_password = sha256_crypt.hash(password)
                    user.password = new_password
                    db.session.commit()
                    session.clear()
                    flash("نیاز به لاگین مجدد با پسورد جدید دارید", "success")
                    return redirect("/login/redirect=&")
            else:
                flash("رمز قدیمی اشتباه است", "error")

        return render_template("changePassword.html", form=form)
    else:
        flash("برای تغییر پسورد ابتدا لاگین کنید", "error")
        return redirect("/login/redirect=changepassword")