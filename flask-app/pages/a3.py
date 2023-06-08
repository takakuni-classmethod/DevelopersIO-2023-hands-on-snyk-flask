from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "a3", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A3")
def a3():
    return render_template("a3.html")