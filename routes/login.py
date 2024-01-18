from helpers import (
    session,
    request,
    sqlite3,
    flash,
    redirect,
    addPoints,
    render_template,
    Blueprint,
    loginForm,
    sha256_crypt,
)
from config import LOG_IN

from models import User, Post, Comment, db


loginBlueprint = Blueprint("login", __name__)


@loginBlueprint.route("/login/redirect=<direct>", methods=["GET", "POST"])
def login(direct):
    direct = direct.replace("&", "/")
    match LOG_IN:
        case True:
            match "userName" in session:
                case True:
                    return redirect(direct)
                case False:
                    form = loginForm(request.form)
                    if request.method == "POST":
                        userName = request.form["userName"]
                        password = request.form["password"]
                        userName = userName.replace(" ", "")
                        user = User.query.filter_by(userName=userName.lower()).first()
                        if not user:
                            flash("یوز پیدا نشد", "error")
                        else:
                            if sha256_crypt.verify(password, user[3]):
                                session["userName"] = user.userName
                                addPoints(1, session["userName"])
                                flash(f"خوشامدید {user[1]}", "success")
                                return redirect(direct)
                            else:
                                flash("پسورد اشتباه است", "error")
                    return render_template("login.html", form=form, hideLogin=True)
        case False:
            return redirect(direct)
