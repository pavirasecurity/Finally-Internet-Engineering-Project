from helpers import (
    ssl,
    flash,
    smtplib,
    randint,
    sqlite3,
    request,
    redirect,
    Blueprint,
    EmailMessage,
    sha256_crypt,
    render_template,
    passwordResetForm,
)

from models import User, Post, Comment, db


passwordResetBlueprint = Blueprint("passwordReset", __name__)


@passwordResetBlueprint.route(
    "/passwordreset/codesent=<codeSent>", methods=["GET", "POST"]
)
def passwordReset(codeSent):
    global userName
    global passwordResetCode
    form = passwordResetForm(request.form)
    match codeSent:
        case "true":
            if request.method == "POST":
                code = request.form["code"]
                password = request.form["password"]
                passwordConfirm = request.form["passwordConfirm"]
                match code == passwordResetCode:
                    case True:
                        user = User.query.filter_by(username=UserName)
                        oldPassword = user.password
                        match password == passwordConfirm:
                            case True:
                                match sha256_crypt.verify(password, oldPassword):
                                    case True:
                                        flash(
                                            "پسورد قدیمی و جدید نباید یکی باشند",
                                            "error",
                                        )
                                    case False:
                                        password = sha256_crypt.hash(password)
                                        user.password = password
                                        db.session.commit()
                                        flash(
                                            "شما با پسورد جدید دوباره لاگین کنید",
                                            "success",
                                        )
                                        return redirect("/login/redirect=&")
                            case False:
                                flash("پسوردها یکسان نیست", "error")
                    case False:
                        flash("کد اشتباه است", "error")
            return render_template("passwordReset.html", form=form, mailSent=True)
        case "false":
            if request.method == "POST":
                userName = request.form["userName"]
                email = request.form["email"]
                userName = userName.replace(" ", "")
                user = User.query.filter_by(userName=UserName)
                userNameDB = user.UserName
                emailDB = user.email
                match not userNameDB or not emailDB:
                    case False:
                        port = 587
                        smtp_server = "smtp.gmail.com"
                        context = ssl.create_default_context()
                        server = smtplib.SMTP(smtp_server, port)
                        server.ehlo()
                        server.starttls(context=context)
                        server.ehlo()
                        server.login(
                            "test-email@gmail.com", "pass-test"
                        )
                        passwordResetCode = str(randint(1000, 9999))
                        message = EmailMessage()
                        message.set_content(
                            f"Hi {userName}👋,\nکد تایید شما🔢:\n{passwordResetCode}"
                        )
                        message.add_alternative(
                            f"""\
                        <html>
                            <body>
                                <h2>سلام {userName}👋,</h2>
                                <h1>{passwordResetCode}</h1>
                                </body>
                        </html>
                        """,
                            subtype="html",
                        )
                        message["Subject"] = "فراموشی رمز عبور"
                        message["From"] = "test-email@gmail.com"
                        message["To"] = email
                        server.send_message(message)
                        server.quit()
                        flash("کد ارسال شد", "success")
                        return redirect("/passwordreset/codesent=true")
                    case True:
                        flash("یوزر پیدا نشد", "error")
            return render_template("passwordReset.html", form=form, mailSent=False)
