from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    make_response
)
from models import get_user_by_password
from utils import (
    generate_session,
    parse_session
)

bp = Blueprint(
    "a2", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A2")
def a2():
    return render_template("a2.html")

@bp.route("/A2/auth", methods=['POST'])
def a2_auth():
    username = request.form.get("username")
    password = request.form.get("password")
    user = get_user_by_password(username, password)
    if not user:
        return render_template("error.html", message="Invalid Crendentials")

    # Generate SessionID
    session_id = generate_session(username)
    response = make_response(redirect("/owasp/A2/welcome"))
    response.set_cookie("sessionId", session_id)

    return response

@bp.route("/A2/welcome")
def a2_welcome():
    if not request.cookies.get("sessionId"):
        return ("<h1>Not Authorized!</h1>")
    session_obj = parse_session(request.cookies.get("sessionId"))
    
    return render_template("welcome.html", username=session_obj['username'])