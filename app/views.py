"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db, login_manager
import smtplib
from datetime import *
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import UserForm
from app.models import userprofile
from werkzeug.utils import secure_filename
from flask import jsonify
from flask import session

UPLOAD_FOLDER = 'app/static/img/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST', 'GET'])
def home():
    form = UserForm()
    """Render profile page."""
    return render_template('profile.html',form=form)
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/profile',methods=['GET','POST'])
def profile():
    form = UserForm(request.form)
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filepath = os.path.join('static/img/', filename)
        user = userprofile((form.firstname.data).title(), (form.lastname.data).title(), form.gender.data, form.email.data, form.location.data, form.biography.data, filepath)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('profiles'))
        #return "User was successfully added"
    else:
        return render_template('profile.html',form=form, filename=filename)
        
@app.route('/profiles')
def profiles():
    """Render the website's profile page."""
    return render_template('profiles.html', users = userprofile.query.all())

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route("/addUser", methods=["GET", "POST"])
def login():
    form = UserForm()
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit(): #if form.username.data:
            # Get the username and password values from the form.
            if (UserProfile.query.filter_by(firstname = form.firstname.data).first() is None):
                
             firstname = form.firstname.data
             lastname = form.lastname.data
             email = form.email.data
             location = form.location.data
             gender = form.gender.data
             biography = form.biography.data
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.
             user = UserProfile(1,firstname,lastname,gender,email,location,biography).first()
             db.session.add(user)
             db.session.commit()
        """ if user is not None:
            # get user id, load into session
             login_user(user)"""
            # remember to flash a message to the user
            
        """ flash('Logged in successfully.', 'success')
             return redirect(url_for("secure_page")) # they should be redirected to a secure-page route instead
            else:
             flash('Username/Password is incorrect.', 'danger')"""
        return redirect(url_for("upload"))
    return render_template("home.html", form=form)

@app.route('/secure-page/')
@login_required
def secure_page():
    if current_user.is_authenticated:
        return render_template('secure_page.html')
    else:
        return render_template('login.html')
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port="8080")
