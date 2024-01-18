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
    signUpForm,
    sha256_crypt,
)
from config import REGISTRATION
from models import User, Post, Comment, db


signUpBlueprint = Blueprint("signup", __name__)


@signUpBlueprint.route("/signup", methods=["GET", "POST"])
def signup():
    match REGISTRATION:
        case True:
            match "userName" in session:
                case True:
                    return redirect("/")
                case False:
                    form = signUpForm(request.form)
                    if request.method == "POST":
                        userName = request.form["userName"]
                        email = request.form["email"]
                        password = request.form["password"]
                        passwordConfirm = request.form["passwordConfirm"]
                        userName = userName.replace(" ", "")
                        users = User.query.all()
                        user = User.query.filter_by(userName=userName.lower()).first()
                        if not userName in users:
                            if passwordConfirm == password:
                                match userName.isascii():
                                    case True:
                                        password = sha256_crypt.hash(password)
                                        newUser = User(
                                            userName=userName.lower(),
                                            email=email,
                                            password=password, 
                                            profilePicture= f"https://api.dicebear.com/7.x/identicon/svg?seed={userName}&radius=10",
                                            role="user",
                                            points=0,
                                            creationDate=currentDate(),
                                            creationTime=currentTime(),
                                            isVerfied="False"
                                            )
                                        db.session.add(newUser)
                                        db.session.commit()
                                        session["userName"] = userName
                                        addPoints(1, session["userName"])
                                        flash(f"خوشامدید {userName}", "success")
                                        return redirect("/verifyUser/codesent=false")
                                    case False:
                                        flash(
                                            "یوزرنیم به درستی وارد نشده",
                                            "error",
                                        )
                            elif passwordConfirm != password:
                                flash("پسوردها یکسان نیستند", "error")
                        elif userName in users:
                            flash("یوزرنیم و ایمیل پیدا نشد", "error")
                        elif not userName in users:
                            flash("ایمیل یافت نشد", "error")
                        elif userName in users:
                            flash("یوزرنیم پیدا نشد", "error")
                    return render_template("signup.html", form=form, hideSignUp=True)
        case False:
            return redirect("/")
