from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    PasswordField,
    SubmitField
)
from wtforms.validators import DataRequired

class Login(FlaskForm):
     user_name=StringField(
       "Username",
       validators=[DataRequired()]
    )
     password=PasswordField(
     "Password",
      validators=[DataRequired()]  
    )
     submit=SubmitField("Login")