from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from mongo_handler import *

# register blueprint definition
registerBlueprint = Blueprint(
    'register',
    __name__,
    static_folder='static',
    static_url_path='/register',
    template_folder='templates'
)


@registerBlueprint.route('/register', methods=['GET', 'POST'])
def register():
    session['pagename'] = 'register'
    if request.method == 'POST':
        if not check_if_registered(request.form.get('email')):
            create_user(request.form.get('email'),
                        request.form.get('password'),
                        request.form.get('fName'),
                        request.form.get('lName'),
                        request.form.get('occupation'),
                        request.form.get('gender'),
                        request.form.get('age')
                        )
            return redirect(url_for('login.login'))
        else:
            message = "This email is already registered."
            #fix css and stuff
            return render_template('register.html', msg=message)
    return render_template('register.html', msg='')
