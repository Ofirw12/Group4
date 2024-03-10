from flask import Blueprint, render_template,session, redirect, url_for, flash,request,jsonify

# will be replaced with sql later
budgets = ["October 2023", "February 2024", "Thailand 2025"]

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
    return render_template('register.html')


