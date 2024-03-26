
from flask import Blueprint, render_template,session, redirect, url_for, flash,request
from mongo_handler import *
# about blueprint definition
friendsBlueprints = Blueprint(
    'friends',
    __name__,
    static_folder='static',
    static_url_path='/friends',
    template_folder='templates'
)


def get_friend_requests(all_my_friends, my_email):
    friend_requests = []
    users_requests = []
    for friend in all_my_friends:
        if friend['Status'] == "Requested":
            friend_requests.append(friend)
    for friend in friend_requests:
        if friend['Email1'] == my_email:
            user = get_user_by_email(friend['Email2'])
            users_requests.append({
                "email": friend['Email2'],
                "first_name": user['FirstName'],
                "last_name": user['LastName'],
            })
        else:
            user = get_user_by_email(friend['Email1'])
            users_requests.append({
                "email": friend['Email1'],
                "first_name": user['FirstName'],
                "last_name": user['LastName'],
            })
    return users_requests


def get_approved_friends(all_my_friends,my_email):
    approved_friends = []
    users = []
    for friend in all_my_friends:
        if friend['Status'] == "Approved":
            approved_friends.append(friend)
    for friend in approved_friends:
        if friend['Email1'] == my_email:
            user = get_user_by_email(friend['Email2'])
            users.append({
                "email": friend['Email2'],
                "first_name": user['FirstName'],
                "last_name": user['LastName'],
                "friends_since": friend['FriendsSince']
            })
        else:
            user = get_user_by_email(friend['Email1'])
            users.append({
                "email": friend['Email1'],
                "first_name": user["FirstName"],
                "last_name": user["LastName"],
                "friends_since": friend['FriendsSince']
            })

    return users



@friendsBlueprints.route('/friends' ,methods=['GET','POST'])
def friends():
    session['pagename'] = 'friends'
    my_email = session['email']
    msg = ""
    if request.method == 'POST':
        user_email = request.form['email']
        if user_email == my_email:
            msg = "this is your own email don't be silly"
        elif check_if_registered(user_email) :
            # להכניס בדיקה שהמייל לא קיים כבר בחברים שלי,ושהמייל לא יוסף לטבלת בקשות חברות מחברים שלי
            add_friend(my_email, user_email)
            msg = "Your friend request has been sent successfully"
        else:
            msg = "Sorry that email is not registered"
        # friend_to_request_email = request.form['email']
        # add_friend(my_email,friend_to_request_email)
        # msg = f"your request to {friend_to_request_email} was sent successfully"

    all_my_friends = get_friends(my_email)
    approved = get_approved_friends(all_my_friends, my_email)
    requested = get_friend_requests(all_my_friends, my_email)
    return render_template("friends.html", approved=approved, requested=requested, my_approved_friends=len(approved), msg=msg)

@friendsBlueprints.route('/friends/<user>/<response>')
def friends_request(response, user):
    if response == "V":
        approve_or_reject_friend_request(session['email'], user, "Approved")
    elif response == "X":
        approve_or_reject_friend_request(session['email'], user, "Rejected")
    return redirect(url_for('friends.friends'))

