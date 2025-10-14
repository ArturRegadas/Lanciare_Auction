from flask import Blueprint, Response, url_for, redirect, request
from myapp.services.CreateUser import create_user
from myapp.services.Messages import auth_message
from myapp.utils.AuthPending import *
from myapp.models.Users import users
from werkzeug.security import generate_password_hash
from secrets import token_hex
from typing import Dict, Any, Tuple

auth_bp = Blueprint("auth", __name__)


def wait_sing_in() -> Response:
    return redirect(
        url_for(
            "waitingPage.WaitingPage",
            type='sing_in',
            _external=True
        )
    )

def wait_resend(email:str) -> Response:
    return redirect(
        url_for(
            "waitingPage.WaitingPage",
            type = "resend",
            email = email,
            _external=True
            )
        )

def login() -> Response:
    return redirect(url_for("loginPage.LoginPage"))

def sing_in() -> Response:
    return redirect(url_for("singInPage.SingInPage"))


@auth_bp.route("/auth/set/<string:token>", methods = ["POST", "GET"])
def auth(token:str) -> Response:
    data = get_by_pending(token)

    if (not data): #not token
        return sing_in()

    new_password = request.form.get("new_password", None)
    user = users.get_by_email(
        data.get("email")
    )

    if (not user): 
        return sing_in()
    
    #change password
    if (new_password):
        user.save_password(new_password)
    #new user
    else:
        create_user(data)
    pop_by_pending(token)
    return login()

@auth_bp.route("/auth/change/<string:email>")
def changePassword(email:str) -> Response:
    token = get_by_emails_dict(email)

    if (not token):
        if(not users.get_by_email(email)):
            return sing_in()
        
        token = add_in({"email": email})
        auth_message(
            email = email,
            content = url_for("changePassword.ChangePassword",token=token, _external=True)
        )
        return wait_resend(email)
    
    auth_message(
        email = email,
        content = url_for("changePassword.ChangePassword",token=token, _external=True)
    )
    return wait_resend(email)

        

