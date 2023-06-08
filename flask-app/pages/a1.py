from flask import (
    Blueprint,
    request,
    render_template_string
)

bp = Blueprint(
    "a1", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A1")
def a1():
    ### Server-Side Template Injection
    name = request.args.get("name", "")
    with open("templates/a1.html") as f:
        template = f.read()
    content = template.replace("{{ name }}", name)
    return render_template_string(content)