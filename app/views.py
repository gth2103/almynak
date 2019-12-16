import os
from flask import render_template, Response, request, jsonify, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils  import secure_filename
from flask_mail import Message
from app import *
from app.models import *
from app.forms import *
from app.register import *
from app.events import *
from app.images import *
from app.account import *

brand_path = Base.query.all()[-1].brand

menu = Base.query.all()[-1].menu

tagline = Home.query.all()[-1].tagline

banner = Home.query.all()[-1].banner

background_path = Home.query.all()[-1].background

color_scheme = Base.query.all()[-1].color

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
@login_required
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
@login_required
def upload_image(file):

    global brand_path
    global background_path

    if request.method == "POST":

        if file not in request.files:

            print("No file selected.")

            return redirect(request.url)

        image = request.files[file]

        if image.filename == "":

            print("Image must have a filename.")

            return redirect(request.url)

        if not allowed_images(image.filename):

            print("Image filetype not allowed.")

        else:

            filename  = secure_filename(image.filename)

        full_path = os.path.join(app.config['IMAGE_UPLOADS_FULL'], filename)
        rel_path = os.path.join(app.config['IMAGE_UPLOADS_REL'], filename)


        image.save(full_path)

        print("Image saved.")

        if file == 'brand-image':

            base = Base(brand = rel_path)

            db.session.add(base)
            db.session.commit()

            print(file  +  " added to db.")

            brand_path = Base.query.all()[-1].brand

        elif file == 'background-image':

            home = Home(background = rel_path)

            db.session.add(home)
            db.session.commit()

            print(file  +  " added to db.")

            background_path = Home.query.all()[-1].background

            print(background_path)

        return redirect(request.url)

    return redirect(url_for('home'))

@app.route('/update_text/<page>/<location>', methods=['GET', 'POST'])
@login_required
def update_text(page, location):

    global banner
    global tagline

    if request.method == 'POST':

        if location == 'banner':

            new_text = request.get_data().decode("utf-8")

            home = Home(banner = new_text)

            db.session.add(home)
            db.session.commit()

            print(new_text  +  " added to db.")

            banner = Home.query.all()[-1].banner

        if location == 'tagline':

            new_text = request.get_data().decode("utf-8")

            home = Home(tagline = new_text)

            db.session.add(home)
            db.session.commit()

            print(new_text  +  " added to db.")

            tagline = Home.query.all()[-1].tagline

    return redirect(url_for(page))

@app.route('/update_menu', methods=['GET', 'POST'])
@login_required
def update_menu():

    global menu

    if request.method == 'POST':
        
        json_data = request.get_json()

        base = Base(menu = json_data)

        db.session.add(base)
        db.session.commit()

        print(json.dumps(json_data)  +  " added to db.")

        menu = Base.query.all()[-1].menu

    return jsonify(menu = menu)

@app.route('/update_color', methods=['GET', 'POST'])
@login_required
def update_color():

    global color_scheme

    if request.method == 'POST':
        
        new_color = request.get_data().decode("utf-8")

        base = Base(color = new_color)

        db.session.add(base)
        db.session.commit()

        print(new_color  +  " added to db.")

        color_scheme = Base.query.all()[-1].color

    return color_scheme

@app.route('/send_mail', methods=['GET', 'POST'])
def send_mail():

    if request.method == 'POST':
        
        json_data = request.get_json()
        fname = json_data["fname"]
        lname = json_data["lname"]
        email = json_data["email"]
        subject = json_data["subject"]
        message = json_data["message"]

        recipient = app.config['MAIL_USERNAME']

        msg = Message('[CUBPS] New message: ' + subject, sender=email, recipients=[recipient])
 
        msg.body = 'New message from ' + fname + ' ' + lname + '\n' + email + '\n\n' + message

        mail.send(msg)

        return jsonify(json_data = json_data)

    return redirect(url_for('contact'))

@app.route('/update_account', methods=['GET', 'POST'])
@login_required
def update_account():
    accform = UpdateAccountForm()
    if accform.validate_on_submit():

        found_err, username_err, email_err = validate_account(current_user, accform.username.data, accform.email.data)
        if found_err is True:
            return jsonify(["error", accform.errors, {"username": username_err, "email": email_err}])

        current_user.username = accform.username.data
        current_user.email = accform.email.data

        db.session.add(current_user)
        db.session.commit()
        return jsonify(["success", {"username": accform.username.data, "email": accform.email.data}])
    return jsonify(["error", accform.errors, False])


@app.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    pswform = UpdatePasswordForm()
    if pswform.validate_on_submit():
        update_psw(pswform, current_user)
        return jsonify("Password updated.")
    return jsonify(pswform.errors)


@app.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    db.session.delete(current_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():

    global brand_path
    global menu
    global tagline
    global banner
    global background_path
    global color_scheme

    return render_template('home.html', brand = brand_path, menu = menu, tagline = tagline, banner = banner, background = background_path, color_scheme = color_scheme)

@app.route('/about', methods=['GET', 'POST'])
def about():

    global color_scheme
    global brand_path
    global menu

    return render_template('about.html', brand = brand_path, menu = menu, color_scheme = color_scheme)

@app.route('/members', methods=['GET', 'POST'])
def members():

    global color_scheme
    global brand_path
    global menu

    return render_template('members.html', brand = brand_path, menu = menu, color_scheme = color_scheme)

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():

    global color_scheme
    global brand_path
    global menu

    return render_template('calendar.html', brand = brand_path, menu = menu, color_scheme = color_scheme)

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    global color_scheme
    global brand_path
    global menu

    return render_template('contact.html', brand = brand_path, menu = menu, color_scheme = color_scheme)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    global color_scheme
    global brand_path
    global menu


    accform = UpdateAccountForm()
    pswform = UpdatePasswordForm()

    return render_template('account.html', brand = brand_path, menu = menu, user = current_user, accform = accform, pswform = pswform, color_scheme = color_scheme)

if __name__ == '__main__':
    app.run(debug = True)