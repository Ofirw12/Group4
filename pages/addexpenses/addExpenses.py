from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from mongo_handler import *
# addExpenses blueprint definition
addExpensesBlueprint = Blueprint(
    'addExpenses',
    __name__,
    static_folder='static',
    static_url_path='/addExpenses',
    template_folder='templates'
)


# Routes
@addExpensesBlueprint.route('/add_expenses/<budget_name>', methods=['GET', 'POST'])
def addExpenses(budget_name):
    session['pagename'] = 'addExpenses'
    if request.method == 'POST':
        print(budget_name)
        budget = get_budget_by_email_and_name(session['email'], budget_name)
        create_new_expense(session['email'],
                           budget['BudgetId'],
                           datetime.strptime(request.form.get('date'), '%Y-%m-%d'),
                           request.form.get('category'),
                           request.form.get('eType'),
                           int(request.form.get('price'))
                           )
    return render_template('addExpenses.html', budget_name=budget_name)


@addExpensesBlueprint.route('/delete_expense/<int:expense_id>')
def deleteExpense(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('wisdoms.wisdoms'))
