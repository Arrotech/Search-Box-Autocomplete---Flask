import os
import json
from flask_wtf import FlaskForm
from wtforms import StringField
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)

cities = ["Nakuru", "Nairobi", "Kakamega", "Kisumu", "Kiambu"]

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

if __name__ == '__main__':
    app.run(debug=True)

