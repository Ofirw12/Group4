
from flask import Blueprint, render_template,session, redirect, url_for, flash

# about blueprint definition
friendsBlueprints = Blueprint(
    'friends',
    __name__,
    static_folder='static',
    static_url_path='/friends',
    template_folder='templates'
)







@friendsBlueprints.route('/friends')
def friends():
    session['pagename'] = 'friends'
    return render_template("friends.html")

