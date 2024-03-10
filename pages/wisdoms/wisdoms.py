from flask import Blueprint, render_template,session, redirect, url_for, flash,request,jsonify
from mongo_handler import *
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
    categories = get_categories(session['email'])
    expenses = get_expenses_by_email(session['email'])
    if request.args.get('category'):
        return render_template('wisdoms.html', categories=categories, expenses=expenses, filter=request.args.get('category'))
    return render_template('wisdoms.html', categories=categories, expenses=expenses, filter='All')


