from flask import (
    Blueprint,
    request,
    render_template_string
)

bp = Blueprint(
    "a7", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A7")
def a7():
    ### Cross-Site Scripting (XSS)
    name = request.args.get("name", "")
    with open("templates/a7.html") as f:
        template = f.read()
    content = template.replace("{{ name }}", name)
    
    return render_template_string(content)