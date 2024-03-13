
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


def get_friend_requests(all_my_friends):
    friend_requests = []
    for friend in all_my_friends:
        if friend['Status'] == "Requested":
            friend_requests.append(friend)
    return friend_requests


def get_approved_friends(all_my_friends):
    approved_friends = []
    for friend in all_my_friends:
        if friend['Status'] == "Approved":
            approved_friends.append(friend)
    return approved_friends


@friendsBlueprints.route('/friends')
def friends():
    session['pagename'] = 'friends'
    my_email = session['email']
    all_my_friends = get_friends(my_email)
    approved = get_approved_friends(all_my_friends)
    requested = get_friend_requests(all_my_friends)
    users = []
    for friend in all_my_friends:
        if friend['Email1'] == my_email:
            if friend['Status'] == "Approved":
                approved.append(get_user_by_email(friend["Email2"]))
            elif friend['Status'] == "Requested":
                requested.append(get_user_by_email(friend["Email2"]))
        elif friend['Email2'] == my_email:
            if friend['Status'] == "Approved":
                approved.append(get_user_by_email(friend["Email2"]))
            elif friend['Status'] == "Requested":
                requested.append(get_user_by_email(friend["Email2"]))
        users.append(get_user_by_email(friend['Email1']))
    return render_template("friends.html", approved=approved, requested=requested, my_email=my_email, users=users)


@friendsBlueprints.route('/friends/<user>/<response>')
def friends_request(response, user):
    if response == "V":
        approve_or_reject_friend_request(session['email'], user, "Approved")
    elif response == "X":
        approve_or_reject_friend_request(session['email'], user, "Rejected")
    return redirect(url_for('friends.friends'))
