import random
from app import db
from app.models import *

def validate_account(cur_user, form_username, form_email):
	username_err = ''
	email_err = ''
	found_err = False
	user = User.query.filter_by(username=form_username).first()
	if user is not None and user.id != cur_user.id:
		username_err = 'Please use a different username.'
		found_err = True
	user = User.query.filter_by(email=form_email).first()
	if user is not None and user.id != cur_user.id:
		email_err = 'Please use a different email address.'
		found_err = True
	return found_err, username_err, email_err

def update_psw(pswform, current_user):
	current_user.set_password(pswform.password.data)
	db.session.add(current_user)
	db.session.commit()

def randomString(stringLength=9):
    values = string.ascii_letters + string.digits
    return ''.join(random.choice(values) for i in range(stringLength))


def createDefaultGroup():
	id = random.randint(100000, 999999)
	exists = Group.query.filter_by(id=id).first()
	if exists:
		createDefaultGroup()
	group = Group(id = id, name = str(id), email = 'default@example.com')
	home = Home(background = '/static/images/square.png', banner = 'TITLE HERE', tagline = 'TAGLINE HERE', group_id = id)
	base = BaseConfig(brand = '/static/images/icon-logo.png', menu = { '' : '', '' : '', '' : '', '' : '' }, color = 'light', facebook = 'https://www.facebook.com/#', twitter = 'https://twitter.com/#', instagram = 'https://www.instagram.com/#', group_id = id)
	db.session.add(home)
	db.session.add(base)
	db.session.add(group)
	db.session.commit()
	return id


