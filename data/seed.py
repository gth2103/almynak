from app import db
from app.models import *
from datetime import datetime

#db.drop_all()

admin = User(username='admin', email='admin@example.com', password_hash=generate_password_hash('admin'), group_id = 611102)

#db.session.add(admin)

menu = {

	'About us' : '/about',
	'' : '',
	'Calendar' : '/calendar',
	'Contact' : '/contact'
}

home = Home(background = '/static/images/home.jpeg', banner = 'Columbia University<div>Black Pre-Professional Society</div>', tagline = 'Lorem ipsum dolor sit amet, mei percipit mnesarchum te, albucius phaedrum.', group_id = 611102)
base = BaseConfig(brand = '/static/images/white_cubps_logo.png', menu = menu, color = 'black', facebook = 'https://www.facebook.com/#', twitter = 'https://twitter.com/#', instagram = 'https://www.instagram.com/#', group_id = 611102)
cubps = Group(id = 611102, name = 'Columbia Black Pre-Professional Society', email = 'gth2103@columbia.edu')

#db.session.add(home)
#db.session.add(base)
#db.session.add(cubps)

#db.session.commit()
