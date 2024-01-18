from helpers import (
    ssl,
    flash,
    smtplib,
    randint,
    sqlite3,
    request,
    session,
    redirect,
    Blueprint,
    EmailMessage,
    render_template,
    verifyUserForm,
)

from models import User, Post, Comment, db


verifyUserBlueprint = Blueprint("verifyUser", __name__)


@verifyUserBlueprint.route("/verifyUser/codesent=<codeSent>", methods=["GET", "POST"])
def verifyUser(codeSent):
    match "userName" in session:
        case True:
            userName = session["userName"]
            user = User.query.filter_by(userName=userName.lower()).first()
            isVerfied = user.isVerfied
            match isVerfied:
                case "True":
                    return redirect("/")
                case "False":
                    global verificationCode
                    form = verifyUserForm(request.form)
                    match codeSent:
                        case "true":
                            if request.method == "POST":
                                code = request.form["code"]
                                match code == verificationCode:
                                    case True:
                                        user.isVerfied = "True"
                                        db.session.commit()
                                        flash(
                                            "اکانت شما تایید شد",
                                            "success",
                                        )
                                        return redirect("/")
                                    case False:
                                        flash("کد اشتباه است", "error")
                            return render_template(
                                "verifyUser.html", form=form, mailSent=True
                            )
                        case "false":
                            if request.method == "POST":
                                user = User.query.filter_by(userName=userName).first()
                                email = user.email
                                match not userNameDB:
                                    case False:
                                        port = 587
                                        smtp_server = "smtp.gmail.com"
                                        context = ssl.create_default_context()
                                        server = smtplib.SMTP(smtp_server, port)
                                        server.ehlo()
                                        server.starttls(context=context)
                                        server.ehlo()
                                        server.login(
                                            "test-email@gmail.com",
                                            "pass-test",
                                        )
                                        verificationCode = str(randint(1000, 9999))
                                        message = EmailMessage()
                                        message.set_content(
                                            f"Hi {userName}👋,\nکد تایید اکانت شما🔢:\n{verificationCode}"
                                        )
                                        message.add_alternative(
                                            f"""\
                                        <html>
                                            <body>
                                                <h2>سلام{userName}👋,</h2>
                                                <h3>کد تایید اکانت شما:</h3>
                                                <h1>{verificationCode}</h1>
                                                </body>
                                        </html>
                                        """,
                                            subtype="html",
                                        )
                                        message["Subject"] = "کدتایید اکانت🔢"
                                        message[
                                            "From"
                                        ] = "flask-test-email@gmail.com"
                                        message["To"] = email
                                        server.send_message(message)
                                        server.quit()
                                        flash("کد ارسال شد", "success")
                                        return redirect("/verifyUser/codesent=true")
                                    case True:
                                        flash("یوزر پیدا نشد", "error")
                            return render_template(
                                "verifyUser.html", form=form, mailSent=False
                            )
        case False:
            return redirect("/")
