from flask import render_template, Blueprint,redirect, session, url_for, Response

home = Blueprint("changePassword", __name__)

@home.route("/reset/<string:token>")
def ChangePassword(token:str) -> Response:
    return render_template("ChangePasswordPage.html", token=token)


