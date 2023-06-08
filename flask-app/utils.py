import json
import base64
from datetime import datetime, timezone

def generate_session(username):
    ### Generate sessionId
    #username = request.form.get("username")
    session_obj = {"username": username, "timestamp": datetime.now(timezone.utc).isoformat()}
    session_id = base64.b64encode(json.dumps(session_obj).encode("utf-8"))
    return session_id

def parse_session(session_obj):
    ### Parse sessionId
    session_obj = json.loads(base64.b64decode(session_obj).decode("utf-8"))
    return session_obj