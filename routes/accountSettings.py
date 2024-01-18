from helpers import (
    session,
    redirect,
    render_template,
    Blueprint,
    request,
    sqlite3,
)
from delete import deleteUser

from models import *


accountSettingsBlueprint = Blueprint("accountSettings", __name__)

accountSettingsBlueprint.route("/accountsettings", methods=["GET", "POST"])
def accountSettings():
    if "userName" in session:
        user = User.query.filter_by(userName=session["userName"]).first()

        if not user:
            abort(404)

        if request.method == "POST":
            if "userDeleteButton" in request.form:
                deleteUser(user.userName)  
                return redirect("/")
        
        return render_template("accountSettings.html", user=user)
    else:
        return redirect("/login/redirect=&accountsettings")