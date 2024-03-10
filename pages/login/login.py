from flask import Blueprint, render_template,session, redirect, url_for, flash, request

# login blueprint definition
loginBlueprint = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/login',
    template_folder='templates'
)


@loginBlueprint.route('/login')
def login():
    session['pagename'] = 'login'
    return render_template("login.html")
