from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.database.models import User

users = User.objects.all()


class TaskForm(FlaskForm):
    task_name = StringField("Task Name",
                           validators=[DataRequired(), Length(min=1, max=20)])
    user_choice = SelectField("Starting User", choices=[(user.id, user.name) for user in users], validators=[DataRequired()])
    submit = SubmitField("Submit")