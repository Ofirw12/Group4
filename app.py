from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'blablabla'
##app.config.from_pyfile('settings.py')


# will be replaced with sql later
budgets = ["October 2023", "February 2024", "Thailand 2025"]

# @app.route("/")
# def home():
#     session["pagename"] = 'home'
#     print(session["pagename"])
#     if request.args.get('Budget'):
#         budget = request.args.get('Budget')
#         return redirect(url_for('addExpenses', budget=budget))
#     return render_template("home.html", budgets=budgets)
#
#
# @app.route('/friends')
# def friends():
#     session['pagename'] = 'friends'
#     return render_template("friends.html")
#
#
# @app.route('/new_budget', methods=['GET', 'POST'])
# def newBudget():
#     session['pagename'] = 'newBudget'
#     if request.method == "POST":
#         newbudget = request.form.get('budgetName')
#         budgets.append(newbudget)
#         return redirect(url_for('home'))
#     return render_template("newBudget.html")
#
#
# @app.route('/login')
# def login():
#     session['pagename'] = 'login'
#     return render_template("login.html")
#
#
@app.route('/logout')
def logout():
    return redirect(url_for('login.login'))

#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     session['pagename'] = 'register'
#     return render_template('register.html')
#
#
# @app.route('/add_expenses/<budget>', methods=['GET', 'POST'])
# def addExpenses(budget):
#     session['pagename'] = 'addExpenses'
#     return render_template('addExpenses.html', budget=budget)
#
#
# @app.route('/wisdoms')
# def wisdoms():
#     session['pagename'] = 'wisdoms'
#     return render_template('wisdoms.html')


##### Pages
# addexpenses
from pages.addexpenses.addExpenses import addExpensesBlueprint

app.register_blueprint(addExpensesBlueprint)

## friends
from pages.friends.friends import friendsBlueprints

app.register_blueprint(friendsBlueprints)

## home
from pages.home.home import homeBlueprint

app.register_blueprint(homeBlueprint)

## login
from pages.login.login import loginBlueprint

app.register_blueprint(loginBlueprint)

## newBudget
from pages.newBudget.newBudget import newBudgetBlueprint

app.register_blueprint(newBudgetBlueprint)

## register
from pages.register.register import registerBlueprint

app.register_blueprint(registerBlueprint)

## wisdom
from pages.wisdoms.wisdoms import wisdomsBlueprint

app.register_blueprint(wisdomsBlueprint)

if __name__ == "__main__":
    app.run(debug=True)
