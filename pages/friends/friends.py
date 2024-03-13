
from flask import Blueprint, render_template,session, redirect, url_for, flash
from mongo_handler import *
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
    my_email = session['email']
    all_my_friends = get_friends(my_email)
    users =[]
    for friend in all_my_friends:
        if friend['Email1'] == my_email:
            users.append(get_user_by_email(friend["Email2"]))
        elif friend['Email2'] == my_email:
            users.append(get_user_by_email(friend['Email1']))
    return render_template("friends.html", all_my_friends=all_my_friends, my_email=my_email, users=users)

