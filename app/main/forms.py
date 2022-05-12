from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write down your bio...',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title=StringField('Pitch title',validators=[DataRequired()])
    pitch=TextAreaField('Pitch description.',validators = [DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Pitch comment.',validators = [DataRequired()])
    submit = SubmitField('Submit')