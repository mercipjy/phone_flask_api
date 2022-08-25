from flask import Blueprint

# Create Blueprint
auth = Blueprint('auth', __name__)

# route
@auth.route('/sign-in')
def sign_in():
    return "<p>Sign-In</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-Up</p>" 