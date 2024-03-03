from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'blablabla'

@app.route("/")
def home():
    session["pagename"] = 'home'
    print(session["pagename"])
    if request.args.get('Budget'):
        budget = request.args.get('Budget')
        return redirect(url_for('addExpenses', budget=budget))
    return render_template("home.html")


@app.route('/friends')
def friends():
    session['pagename'] = 'friends'
    return render_template("friends.html")


@app.route('/new_budget')
def newBudget():
    session['pagename'] = 'newBudget'
    return render_template("newBudget.html")


@app.route('/login')
def login():
    session['pagename'] = 'login'
    return render_template("login.html")


@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    session['pagename'] = 'register'
    return render_template('register.html')


@app.route('/add_expenses/<budget>', methods=['GET', 'POST'])
def addExpenses(budget):
    session['pagename'] = 'addExpenses'
    return render_template('addExpenses.html', budget=budget)

@app.route('/wisdoms')
def wisdoms():
    session['pagename'] = 'wisdoms'
    return render_template('wisdoms.html')


if __name__ == "__main__":
    app.run(debug=True)
