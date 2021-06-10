from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

## Create Post Form
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


## Registration Form
class RegisterForm(FlaskForm):
    name = StringField(label="Username:", validators=[DataRequired()])
    email = StringField(label="Email:", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password:", validators=[DataRequired(), Length(min=8, message="Please create a password with at least 8 characters.")])
    submit = SubmitField(label="Register")

# Login Form
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

# Comment Form
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


