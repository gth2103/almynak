from app import db
from app.models import *
from datetime import datetime

#db.drop_all()

admin = User(username='admin', email='gth2103@columbia.edu', password_hash=generate_password_hash('admin'))
guest = User(username='guest', email='guest@columbia.edu', password_hash=generate_password_hash('guest'))
grant =  User(username='grant', email='grant@columbia.edu', password_hash=generate_password_hash('grant'))
john =  User(username='john', email='john@columbia.edu', password_hash=generate_password_hash('john'))
jane =  User(username='jane', email='jane@columbia.edu', password_hash=generate_password_hash('jane'))

#db.session.add(admin)
#db.session.add(guest)
#db.session.add(grant)
#db.session.add(john)
#db.session.add(jane)
#db.session.commit()


event1 = Event(id='1', title='example1', comment='', group='event-success', start_date=datetime(2019, 11, 20, 20, 00, 00), end_date=datetime(2019, 11, 20, 20, 1, 2))
event2 = Event(id='2', title='example2', comment='', group='event-important', start_date=datetime(2019, 11, 25, 19, 00, 00), end_date=datetime(2019, 11, 25, 19, 42, 45))
event3 = Event(id='3', title='example3', comment='', group='event-info', start_date=datetime(2019, 11, 13, 20, 3, 5), end_date=datetime(2019, 11, 14, 8, 45, 53))
event4 = Event(id='4', title='example4', comment='', group='event-error', start_date=datetime(2019, 11, 14, 20, 3, 5), end_date=datetime(2019, 11, 15, 8, 45, 53))

#db.session.add(event1)
#db.session.add(event2)
#db.session.add(event3)
#db.session.add(event4)
#db.session.commit()

menu1 = {

	'About us' : '/about',
	'Members' : '/members',
	'Calendar' : '/calendar',
	'Contact' : '/contact'
}

home1 = Home(brand = '/static/images/white_cubps_logo.png', banner = 'Columbia University<div>Black Pre-Professional Society</div>', tagline = 'Lorem ipsum dolor sit amet, mei percipit mnesarchum te, albucius phaedrum.', menu = menu1)

db.session.add(home1)
db.session.commit()
