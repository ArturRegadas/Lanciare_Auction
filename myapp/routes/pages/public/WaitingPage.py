from flask import Blueprint, render_template

waiting_page_bp = Blueprint("waitingPage", __name__)

@waiting_page_bp.route("/waitingPage")
@waiting_page_bp.route("/waitingPage/<string:type>/")
@waiting_page_bp.route("/waitingPage/<string:type>/<string:email>")
def WaitingPage(type:str = "sing_in", email=""):
    return render_template("Waiting.html", type = type, email = email)
