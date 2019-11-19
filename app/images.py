from app import app

def allowed_images(filename):

	if not "." in filename:
		return False

	ext = filename.rsplit(".", 1)[1]

	if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
		return True
	else:
		return  False