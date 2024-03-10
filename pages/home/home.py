
from flask import Blueprint, render_template,session, redirect, url_for, flash , request

# about blueprint definition
homeBlueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    static_url_path='/home',
    template_folder='templates'
)
# will be replaced with sql later
budgets = ["October 2023", "February 2024", "Thailand 2025"]

@homeBlueprint.route("/")
def home():
    session["pagename"] = 'home'
    print(session["pagename"])
    if request.args.get('Budget'):
        budget = request.args.get('Budget')
        return redirect(url_for('addExpenses.addExpenses', budget=budget))
    return render_template("home.html", budgets=budgets)

