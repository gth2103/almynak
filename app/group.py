from app.models import *

def get_base_config(gid):

	brand_path = BaseConfig.query.filter_by(group_id=gid).all()[-1].brand
	menu = BaseConfig.query.filter_by(group_id=gid).all()[-1].menu
	theme_color = BaseConfig.query.filter_by(group_id=gid).all()[-1].color
	facebook_url = BaseConfig.query.filter_by(group_id=gid).all()[-1].facebook
	twitter_url = BaseConfig.query.filter_by(group_id=gid).all()[-1].twitter
	instagram_url = BaseConfig.query.filter_by(group_id=gid).all()[-1].instagram

	return brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url

def get_home_config(gid):

	tagline = Home.query.filter_by(group_id=gid).all()[-1].tagline
	banner = Home.query.filter_by(group_id=gid).all()[-1].banner
	background_path = Home.query.filter_by(group_id=gid).all()[-1].background

	return tagline, banner, background_path

