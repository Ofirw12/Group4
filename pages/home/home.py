
from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from mongo_handler import *
# about blueprint definition
homeBlueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    static_url_path='/home',
    template_folder='templates'
)


@homeBlueprint.route("/")
def home():
    session["pagename"] = 'home'
    if request.args.get('Budget'):
        budget = request.args.get('Budget')
        return redirect(url_for('addExpenses.addExpenses', budget_name=budget))
    budgets = get_budgets_names(session['email'])
    return render_template("home.html", budgets=budgets, name=session['usersname'])

