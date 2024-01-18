
from helpers import (
    render_template,
    getProfilePicture,
    Flask,
)

from routes.post import postBlueprint
from routes.user import userBlueprint
from routes.index import indexBlueprint
from routes.login import loginBlueprint
from routes.signup import signUpBlueprint
from routes.logout import logoutBlueprint
from routes.search import searchBlueprint
from routes.editPost import editPostBlueprint
from routes.searchBar import searchBarBlueprint
from routes.dashboard import dashboardBlueprint
from routes.verifyUser import verifyUserBlueprint
from routes.adminPanel import adminPanelBlueprint
from routes.createPost import createPostBlueprint
from routes.sociallogin import loginGoogleBlueprint
from routes.passwordReset import passwordResetBlueprint
from routes.changeUserName import changeUserNameBlueprint
from routes.changePassword import changePasswordBlueprint
from routes.adminPanelUsers import adminPanelUsersBlueprint
from routes.adminPanelPosts import adminPanelPostsBlueprint
from routes.accountSettings import accountSettingsBlueprint
from routes.adminPanelComments import adminPanelCommentsBlueprint
from routes.changeProfilePicture import changeProfilePictureBlueprint

from flask_wtf.csrf import CSRFProtect, CSRFError
from models import *

from config import (
    APP_HOST,
    DEBUG_MODE,
    LOG_IN,
    REGISTRATION,
    APP_SECRET_KEY,
    SESSION_PERMANENT,
    SQLALCHEMY_DATABASE_URI,
)

app = Flask(__name__, template_folder="templates/", static_folder="static/")
app.secret_key = APP_SECRET_KEY
app.config["SESSION_PERMANENT"] = SESSION_PERMANENT
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI 
csrf = CSRFProtect(app)
db.init_app(app)

@app.context_processor
def utility_processor():
    getProfilePicture
    return dict(getProfilePicture=getProfilePicture)


@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template("csrfError.html", reason=e.description), 400


app.register_blueprint(postBlueprint)
app.register_blueprint(userBlueprint)
app.register_blueprint(indexBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(signUpBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(searchBlueprint)
app.register_blueprint(editPostBlueprint)
app.register_blueprint(dashboardBlueprint)
app.register_blueprint(searchBarBlueprint)
app.register_blueprint(adminPanelBlueprint)
app.register_blueprint(createPostBlueprint)
app.register_blueprint(verifyUserBlueprint)
app.register_blueprint(loginGoogleBlueprint)
app.register_blueprint(setUserRoleBlueprint)
app.register_blueprint(passwordResetBlueprint)
app.register_blueprint(changeUserNameBlueprint)
app.register_blueprint(changePasswordBlueprint)
app.register_blueprint(adminPanelUsersBlueprint)
app.register_blueprint(adminPanelPostsBlueprint)
app.register_blueprint(accountSettingsBlueprint)
app.register_blueprint(adminPanelCommentsBlueprint)
app.register_blueprint(changeProfilePictureBlueprint)


match __name__:
    case "__main__":
        app.run(debug=DEBUG_MODE, host=APP_HOST)
