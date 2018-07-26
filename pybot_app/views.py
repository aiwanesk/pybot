""" Views function """
from flask import render_template, url_for, flash, redirect
from pybot_app import app
from pybot_app.form import AddressForm
from pybot_app.parser import Parser


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    if form.validate_on_submit():
        address_ask = Parser(form.address.data)
        flash('Votre demande : {}'.format(form.address.data))
        flash('Ma demande par la classe : ' + address_ask.cut_sentence())
        return redirect(url_for('index'))
    return render_template('index.html', form=form)