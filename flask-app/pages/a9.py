from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "a9", __name__,
    template_folder='templates',
    static_folder='static'
)
@bp.route("/A9")
def a9():
    return render_template("a9.html")