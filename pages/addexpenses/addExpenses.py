from flask import Blueprint, render_template, session, redirect, url_for, flash

# addExpenses blueprint definition
addExpensesBlueprint = Blueprint(
    'addExpenses',
    __name__,
    static_folder='static',
    static_url_path='/addExpenses',
    template_folder='templates'
)


# Routes
@addExpensesBlueprint.route('/add_expenses/<budget>', methods=['GET', 'POST'])
def addExpenses(budget):
    session['pagename'] = 'addExpenses'
    return render_template('addExpenses.html', budget=budget)
