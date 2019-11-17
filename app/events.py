from app import db
from app.models import *

def get_events():
	events = db.session.query(Event).all()
	return events