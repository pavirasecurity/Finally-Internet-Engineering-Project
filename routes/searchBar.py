from helpers import (
    render_template,
    Blueprint,
)

from models import *

searchBarBlueprint = Blueprint("searchBar", __name__)


@searchBarBlueprint.route("/searchbar")
def searchBar():
    return render_template("searchBar.html")
