from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField,FileField,SubmitField
from wtforms.validators import Required, InputRequired

class UserForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('Female','Female')]) 
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Image File', validators=[Required()])
    submit = SubmitField("Register")