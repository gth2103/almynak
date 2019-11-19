import os
from flask import render_template, Response, request, jsonify, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils  import secure_filename
from app import app, db
from app.models import *
from app.forms import *
from app.register import *
from app.events import *
from app.images import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form  = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form  = RegistrationForm()
    if form.validate_on_submit():
        commit_registration(form)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/upload-image/<file>', methods=['GET', 'POST'])
def upload_image(file):

    if request.method == "POST":

        print(file)

        if file not in request.files:

            print("No file selected.")

            return redirect(request.url)

        image = request.files["brand-image"]

        if image.filename == "":

            print("Image must have a filename.")

            return redirect(request.url)

        if not allowed_images(image.filename):

            print("Image filetype not allowed.")

        else:

            filename  = secure_filename(image.filename)


        image.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))

        print("Image saved.")

        return redirect(request.url)

    return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('about.html')

@app.route('/members', methods=['GET', 'POST'])
def members():
    return render_template('members.html')

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template('calendar.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug = True)