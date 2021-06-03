import os
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)

app.secret_key = "secret"

cities = ["Nakuru", "Nairobi", "Kakamega", "Kisumu", "Kiambu"]


class MultipleFieldForm(FlaskForm):
    """Create multiple field select form."""
    language = SelectMultipleField('Programming Languages', choices=[
                                   ('py', 'Python'),
                                   ('jav', 'Java'),
                                   ('cs', 'C #'),
                                   ('cpp', 'C ++'),
                                   ('c', 'C'),
                                   ('html', 'HTML'),
                                   ('js', 'JavaScript'),
                                   ('php', 'PHP')])


@app.route('/')
def upload_form():
    return render_template('autocomplete.html')


@app.route('/search', methods=['POST'])
def search():
    term = request.form['q']

    filtered_cities = [city for city in cities if term.lower() in city.lower()]

    response = jsonify(filtered_cities)
    response.status_code = 200
    return response


@app.route('/multiple_select', methods=['GET', 'POST'])
def multiple_select():
    """Select multiple values."""
    form = MultipleFieldForm()
    language = form.language.data
    return render_template('multiple_select.html', form=form, language=language)


if __name__ == '__main__':
    app.run(debug=True)
