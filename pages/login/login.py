from flask import Blueprint, render_template,session, redirect, url_for, flash, request
from mongo_handler import *
# login blueprint definition
loginBlueprint = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/login',
    template_folder='templates'
)


@loginBlueprint.route('/login', methods=['GET', 'POST'])
def login():
    session['pagename'] = 'login'
    if request.method == 'POST':
        if check_if_registered(request.form.get('email')):
            user = get_user_by_email(request.form.get('email'))
            if user['Password'] == request.form.get('password'):
                session['email'] = request.form.get('email')
                session['usersname'] = user['FirstName']
                return redirect(url_for('home.home'))
            else:
                # wrong password
                pass
        else:
            # no email like this
            pass
    return render_template("login.html")
