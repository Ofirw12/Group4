import os
from datetime import datetime

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from settings import DB_URI

# get your uri from .env file
uri = DB_URI

# create cluster
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)


# get all dbs and collections that needed
db = client['BudgetBunny']
users_col = db['Users']
budgets_col = db['Budgets']
expenses_col = db['Expenses']
friends_of_col = db['Friends']
customers_col = db['BudgetBunny']


def create_user(email,password, fName, lName, occupation, gender, age):
    new_user = {
        'Email': email,
        'Password': password,
        'DateJoined': datetime.today().strftime('%d/%m/%Y'),
        'FirstName': fName,
        'LastName': lName,
        'Occupation': occupation,
        'Gender': gender,
        'Age': age
    }
    users_col.insert_one(new_user)


def check_if_registered(email):
    if get_user_by_email(email):
        return True
    return False


def get_user_by_email(email):
    return users_col.find_one({'Email': email})


def create_budget(email, budget_name, start_time, end_time, budget):
    def get_highest_budget_id():
        budgets = budgets_col.find({})
        highest_budget_id = 1
        for budget in budgets:
            if budget.get('BudgetId') > highest_budget_id:
                highest_budget_id = budget.get('BudgetId')
        return highest_budget_id

    new_budget = {
        'Email': email,
        'BudgetId': get_highest_budget_id() + 1,
        'BudgetName': budget_name,
        'StartTime': start_time.strftime('%d/%m/%Y'),
        'EndTime': end_time.strftime('%d/%m/%Y'),
        'Budget': budget,
    }
    budgets_col.insert_one(new_budget)


def get_budgets_names(email):
    budgets = list(budgets_col.find({'Email': email}))
    return [budget['BudgetName'] for budget in budgets]


def create_new_expense(email, budget_id, expense_date, category, expense_type, price):
    def get_highest_expense_id():
        expenses = expenses_col.find({})
        highest_expense_id = 1
        for expense in expenses:
            if expense.get('ExpenseId') > highest_expense_id:
                highest_expense_id = expense.get('ExpenseId')
        return highest_expense_id

    new_expense = {
        'Email': email,
        'BudgetId': budget_id,
        'ExpenseId': get_highest_expense_id() + 1,
        'Date': expense_date.strftime('%d/%m/%Y'),
        'Category': category,
        'ExpenseType': expense_type,
        'Price': price,
    }
    expenses_col.insert_one(new_expense)


def get_expenses_by_budget_id(budget_id):
    return list(expenses_col.find({'BudgetId': budget_id}))


def get_budget_by_email_and_name(email, name):
    budget = budgets_col.find_one({'Email': email, 'BudgetName': name})
    print(email, name)
    print(budget)
    print(budget['BudgetId'])
    return budget

def test():
    pass
