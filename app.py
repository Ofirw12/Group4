from flask import Flask, render_template, request, redirect, url_for, session
from settings import SECRET_KEY
from mongo_handler import *

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = SECRET_KEY


# will be replaced with sql later
budgets = ["October 2023", "February 2024", "Thailand 2025"]


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.login'))


@app.route('/test')
def mongotest():
    test()
    return redirect(url_for('home.home'))


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
