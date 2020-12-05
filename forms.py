from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoListForm(FlaskForm):
    todotext = StringField('To-do list', validators=[DataRequired()]) 
    submit = SubmitField('Add')