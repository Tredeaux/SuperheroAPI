import requests
from flask import render_template, request, flash
from app import app

API_DOMAIN = 'http://localhost:5000/'


# - CONTROLLER ------------------------------------------------#
#   This is the index page                                     #
# -------------------------------------------------------------#
@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info('INDEX')
    result = None
    if request.method == 'POST':
        search_superhero = request.form.get('superhero')
        if search_superhero:
            data = {'superhero': search_superhero}
            r = requests.post(API_DOMAIN + 'superhero', json=data)
            result = r.text
            print(result)
    return render_template('pages/home.html',
                           result=result)
