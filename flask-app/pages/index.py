from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "index", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/")
def index():
    return render_template("index.html")