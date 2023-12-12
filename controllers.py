import json

import requests
from flask import render_template, request, flash, redirect, url_for
from app import app

API_DOMAIN = 'http://localhost:5000/'


# - CONTROLLER ------------------------------------------------#
#   This is the index page                                     #
# -------------------------------------------------------------#
@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info('INDEX')
    result = None
    id = None
    if request.method == 'POST':
        search_superhero = request.form.get('superhero')
        if search_superhero:
            data = {'superhero': search_superhero}
            r = requests.post(API_DOMAIN + 'superhero', json=data)
            if r.status_code == 200:
                result = r.text
                data = json.loads(r.text)
                if data["message"] == "success":
                    id = data["superhero"]["id"]
    return render_template('pages/home.html',
                           result=result,
                           id=id)


# - CONTROLLER ------------------------------------------------#
#   This handles favourites                                    #
# -------------------------------------------------------------#
@app.route('/favourite-actions', methods=['POST'])
def favourite():
    app.logger.info('FAVOURITE')
    if request.method == 'POST':
        id = request.form.get('superhero')
        if id:
            data = {'id': id}
            headers = {'Content-type': 'application/json'}
            r = requests.post(API_DOMAIN + 'favourite', json=data, headers=headers)
            print(r.text)
            if r.text:
                data = json.loads(r.text)
                if data["message"] == "success":
                    flash('Saved to favourites', 'success')
                    return redirect(url_for('index'))
    flash('something went wrong', 'danger')
    return redirect(url_for('index'))


