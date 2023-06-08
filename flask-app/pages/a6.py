from flask import (
    Blueprint,
    request,
    render_template
)

bp = Blueprint(
    "a6", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A6")
def a6():
    ### A poorly written code can expose a lot of things specially if the DEBUG mode is left on
    ##  FIX: turn over debug mode!
    age = int(request.args.get("age", 0))
    new_age = 0
    if age:
        new_age = age + 1
    return render_template("a6.html", age=new_age)