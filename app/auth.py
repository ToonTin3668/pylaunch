from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    pass
    #return "<p>Login</p>"

@auth.route('/logout')
def logout():
    pass
    #return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    pass
    #return "<p>Sign Up</p>"
