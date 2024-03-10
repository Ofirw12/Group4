from flask import Blueprint, render_template,session, redirect, url_for, flash,request,jsonify

# will be replaced with sql later
budgets = ["October 2023", "February 2024", "Thailand 2025"]

# newBudget blueprint definition
newBudgetBlueprint = Blueprint(
    'newBudget',
    __name__,
    static_folder='static',
    static_url_path='/newBudget',
    template_folder='templates'
)





@newBudgetBlueprint.route('/new_budget', methods=['GET', 'POST'])
def newBudget():
    session['pagename'] = 'newBudget'
    if request.method == "POST":
        newbudget = request.form.get('budgetName')
        budgets.append(newbudget)
        return redirect(url_for('home.home'))
    return render_template("newBudget.html")
