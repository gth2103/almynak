import os, re
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
from app.group import *

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home', current_gid=current_user.group_id))
    form  = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home', current_gid=user.group_id)
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
        return redirect(url_for('home', current_gid=current_user.group_id))
    form  = RegistrationForm()
    if form.validate_on_submit():
        commit_registration(form)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/upload_image/<file>/<page>', methods=['GET', 'POST'])
@login_required
def upload_image(file, page):

    tagline, banner, background_path = get_home_config(current_user.group_id)

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    if request.method == "POST":

        if file not in request.files:

            print("No file selected.")

            return redirect(url_for(page, current_gid=current_user.group_id))

        image = request.files[file]

        if image.filename == "":

            print("Image must have a filename.")

            return redirect(url_for(page, current_gid=current_user.group_id))

        if not allowed_images(image.filename):

            print("Image filetype not allowed.")

        else:

            filename  = secure_filename(image.filename)

        full_path = os.path.join(app.config['IMAGE_UPLOADS_FULL'], filename)
        rel_path = os.path.join(app.config['IMAGE_UPLOADS_REL'], filename)


        image.save(full_path)

        print("Image saved.")

        if file == 'brand-image':

            base = BaseConfig(brand = rel_path, menu = menu, color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id = current_user.group_id)

            db.session.add(base)
            db.session.commit()

            print(file  +  " added to db.")

            brand_path = BaseConfig.query.filter_by(group_id=current_user.group_id).all()[-1].brand

        elif file == 'background-image':

            home = Home(background = rel_path, banner = banner, tagline = tagline, group_id = current_user.group_id)

            db.session.add(home)
            db.session.commit()

            print(file  +  " added to db.")

            background_path = Home.query.filter_by(group_id=current_user.group_id).all()[-1].background

            print(background_path)
            
    return redirect(url_for(page, current_gid=current_user.group_id))

@app.route('/update_text/<page>/<location>', methods=['GET', 'POST'])
@login_required
def update_text(page, location):

    tagline, banner, background_path = get_home_config(current_user.group_id)

    if request.method == 'POST':

        if location == 'banner':

            new_banner = request.get_data().decode("utf-8")

            home = Home(background = background_path, banner = new_banner, tagline = tagline, group_id = current_user.group_id)

            db.session.add(home)
            db.session.commit()

            print(new_banner  +  " added to db.")

            banner = Home.query.filter_by(group_id=current_user.group_id).all()[-1].banner

        if location == 'tagline':

            new_tagline = request.get_data().decode("utf-8")

            home = Home(background = background_path, banner = banner, tagline = new_tagline, group_id = current_user.group_id)

            db.session.add(home)
            db.session.commit()

            print(new_tagline  +  " added to db.")

            tagline = Home.query.filter_by(group_id=current_user.group_id).all()[-1].tagline

    return redirect(url_for(page, current_gid=current_user.group_id))

@app.route('/update_menu', methods=['GET', 'POST'])
@login_required
def update_menu():

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    if request.method == 'POST':
        
        json_data = request.get_json()

        base = BaseConfig(brand = brand_path, menu = json_data, color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id = current_user.group_id)

        db.session.add(base)
        db.session.commit()

        print(json.dumps(json_data)  +  " added to db.")

        menu = BaseConfig.query.filter_by(group_id=current_user.group_id).all()[-1].menu

    return jsonify(menu = menu)

@app.route('/update_color', methods=['GET', 'POST'])
@login_required
def update_color():

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    if request.method == 'POST':
        
        new_color = request.get_data().decode("utf-8")

        base = BaseConfig(brand = brand_path, menu = menu, color = new_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id = current_user.group_id)

        db.session.add(base)
        db.session.commit()

        print(new_color  +  " added to db.")

        theme_color = BaseConfig.query.filter_by(group_id=current_user.group_id).all()[-1].color

    return theme_color

@app.route('/send_mail/<current_gid>', methods=['GET', 'POST'])
def send_mail(current_gid):

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

    return redirect(url_for('contact', current_gid=current_gid))

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

@app.route('/update_facebook', methods=['GET', 'POST'])
@login_required
def update_facebook():

    tagline, banner, background_path = get_home_config(current_user.group_id)

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    if request.method == 'POST':

        url = request.get_data().decode("utf-8")

        pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?www\.facebook\.com\/(?!.*\/).*$'

        if bool(re.match(pattern, url)):

            base = BaseConfig(brand = brand_path, menu = menu, color = theme_color, facebook = url, twitter = twitter_url, instagram = instagram_url, group_id = current_user.group_id)

            db.session.add(base)
            db.session.commit()

            print(url  +  " added to db.")

            facebook_url = BaseConfig.query.filter_by(group_id=current_user.group_id).all()[-1].facebook

    return facebook_url

@app.route('/update_twitter', methods=['GET', 'POST'])
@login_required
def update_twitter():

    tagline, banner, background_path = get_home_config(current_user.group_id)

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    if request.method == 'POST':

        url = request.get_data().decode("utf-8")

        pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?www\.twitter\.com\/(?!.*\/).*$'

        if bool(re.match(pattern, url)):

            base = BaseConfig(brand = brand_path, menu = menu, color = theme_color, facebook = facebook_url, twitter = url, instagram = instagram_url, group_id = current_user.group_id)

            db.session.add(base)
            db.session.commit()

            print(url  +  " added to db.")

            twitter_url = BaseConfig.query.filter_by(group_id=current_user.group_id).all()[-1].twitter

    return twitter_url

@app.route('/update_instagram', methods=['GET', 'POST'])
@login_required
def update_instagram():

    tagline, banner, background_path = get_home_config(current_user.group_id)

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    if request.method == 'POST':

        url = request.get_data().decode("utf-8")

        pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?www\.instagram\.com\/(?!.*\/).*$'

        if bool(re.match(pattern, url)):

            base = BaseConfig(brand = brand_path, menu = menu, color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = url, group_id = current_user.group_id)

            db.session.add(base)
            db.session.commit()

            print(url  +  " added to db.")

            instagram_url = BaseConfig.query.filter_by(group_id=current_user.group_id).all()[-1].instagram

    return instagram_url


@app.route('/<current_gid>')
@app.route('/home/<current_gid>', methods=['GET', 'POST'])
def home(current_gid):

    tagline, banner, background_path = get_home_config(current_gid)

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_gid)

    return render_template('home.html', brand = brand_path, menu = menu, tagline = tagline, banner = banner, background = background_path, theme_color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id=current_gid)

@app.route('/about/<current_gid>', methods=['GET', 'POST'])
def about(current_gid):

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_gid)

    return render_template('about.html', brand = brand_path, menu = menu, theme_color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id=current_gid)

@app.route('/members/<current_gid>', methods=['GET', 'POST'])
def members(current_gid):

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_gid)

    return render_template('members.html', brand = brand_path, menu = menu, theme_color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id=current_gid)

@app.route('/calendar/<current_gid>', methods=['GET', 'POST'])
def calendar(current_gid):

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_gid)

    return render_template('calendar.html', brand = brand_path, menu = menu, theme_color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id=current_gid)

@app.route('/contact/<current_gid>', methods=['GET', 'POST'])
def contact(current_gid):

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_gid)

    return render_template('contact.html', brand = brand_path, menu = menu, theme_color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id=current_gid)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    brand_path, menu, theme_color, facebook_url, twitter_url, instagram_url = get_base_config(current_user.group_id)

    accform = UpdateAccountForm()
    pswform = UpdatePasswordForm()

    return render_template('account.html', brand = brand_path, menu = menu, user = current_user, accform = accform, pswform = pswform, theme_color = theme_color, facebook = facebook_url, twitter = twitter_url, instagram = instagram_url, group_id=str(current_user.group_id))

if __name__ == '__main__':
    app.run(debug = True)