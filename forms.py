from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    """This class creates form for posts"""

    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("SAVE POST")


class RegisterForm(FlaskForm):
    """This class creates form for users registration information"""

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired(), Length(min=8)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    """This class creates form for users information"""

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LET ME IN!")


class CommentForm(FlaskForm):
    """This class creates form for comments"""

    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("SUBMINT COMMENT")
