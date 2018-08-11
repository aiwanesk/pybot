""" Class to create form """

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddressForm(FlaskForm):
    """ Create the form fields """

    input_address = StringField(
        label='Demander une adresse à PyBot',
        render_kw={"placeholder": "Dis-moi PyBot, où se trouve la superbe ville de Toufflers ?"}
    )
    submit = SubmitField('Poser votre question à PyBot !')
