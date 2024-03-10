from flask import Blueprint, render_template,session, redirect, url_for, flash,request,jsonify

# will be replaced with sql later
budgets = ["October 2023", "February 2024", "Thailand 2025"]

# wisdoms blueprint definition
wisdomsBlueprint = Blueprint(
    'wisdoms',
    __name__,
    static_folder='static',
    static_url_path='/wisdoms',
    template_folder='templates'
)

@wisdomsBlueprint.route('/wisdoms')
def wisdoms():
    session['pagename'] = 'wisdoms'
    return render_template('wisdoms.html')


