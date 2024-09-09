from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
    
)
from wtforms.validators import(
    DataRequired,
    length,
    Email,
    Optional,
    EqualTo
    
)

class Signup(FlaskForm):
    username=StringField(
      "username",
      validators=[DataRequired(),length(2,20)]
    )
    email=StringField(
       "Email",
       validators=[DataRequired(),Email()]
    )
    gender=SelectField (
      "Gender",
      choices=["male","female","other"],
      validators=[Optional()]
    )
    dob=DateField(
      "Date of birth",
       validators=[Optional()]
    )
    password=PasswordField(
     "Password",
      validators=[DataRequired(),length(5,20)]  
    )
    confirm_password=PasswordField(
        "Confirm_Password",
        validators=[DataRequired(),length(5,20),EqualTo("password")]
    )
    submit=SubmitField("Sign-Up")
class Login(FlaskForm):
     email=StringField(
       "Email",
       validators=[DataRequired(),Email()]
    )
     password=PasswordField(
     "Password",
      validators=[DataRequired(),length(5,20)]  
    )
     remember_me=BooleanField("Remeber_Me")
     submit=SubmitField("Login")