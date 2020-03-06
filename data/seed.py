from app import db
from app.models import *
from datetime import datetime

#db.drop_all()

admin = User(username='admin', email='admin@example.com', password_hash=generate_password_hash('admin'), group_id = 611102)

db.session.add(admin)

menu = {

	'About us' : '/about',
	'' : '',
	'Calendar' : '/calendar',
	'Contact' : '/contact'
}

home = Home(background = '/static/images/home.jpeg', banner = 'Columbia University<div>Black Pre-Professional Society</div>', tagline = 'Lorem ipsum dolor sit amet, mei percipit mnesarchum te, albucius phaedrum.', group_id = 611102)
base = BaseConfig(brand = '/static/images/white_cubps_logo.png', menu = menu, color = 'black', facebook = 'https://www.facebook.com/#', twitter = 'https://twitter.com/#', instagram = 'https://www.instagram.com/#', group_id = 611102)
cubps = Group(id = 611102, name = 'Columbia Black Pre-Professional Society', email = 'gth2103@columbia.edu')

member1 =  Member(founder = True, name = 'Anita Onyimah', title = 'Co-Founder and CEO', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'aao2126@columbia.edu', coffee = '', group_id = 611102)
member2 =  Member(founder = True, name = 'Yasmeen Metellus', title = 'Co-Founder and CEO', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'ym2558@columbia.edu', coffee = '', group_id = 611102)


member3 =  Member(founder = False, name = 'Layla Alexander', title = 'Chief Executive Officer', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'example1@columbia.edu', coffee = '', group_id = 611102)
member4 =  Member(founder = False, name = 'Zusi Ine', title = 'Chief Marketing Officer', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'example2@columbia.edu', coffee = '', group_id = 611102)
member5 =  Member(founder = False, name = 'Lauren Buehner', title = 'Chief Development Officer', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'example3@columbia.edu', coffee = '', group_id = 611102)
member6 =  Member(founder = False, name = 'Malik Johnson', title = 'Chief Operating Officer', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'example4@columbia.edu', coffee = '', group_id = 611102)
member7 =  Member(founder = False, name = 'Collins Mokua', title = 'Chief Financial Officer', image = '/static/images/board_1.jpeg', about = 'Lorem ipsum dolor sit amet, mei ad modo suscipit, dolores mentitum et vel. Integre necessitatibus eos ut, diam signiferumque ut ius. At vis odio inani nominati, vis veniam democritum abhorreant id. Amet officiis vis id, has ad elaboraret scribentur. No per wisi graeco aliquid, corpora maluisset per in. Utinam percipit theophrastus per cu, pri munere nominati te.', email = 'example5@columbia.edu', coffee = '', group_id = 611102)

#db.session.add(home)
#db.session.add(base)
#db.session.add(cubps)
#db.session.add(member1)
#db.session.add(member2)
#db.session.add(member3)
#db.session.add(member4)
#db.session.add(member5)
#db.session.add(member6)
#db.session.add(member7)

db.session.commit()
