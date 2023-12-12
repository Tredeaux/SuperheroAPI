from flask import Response, request
from app import app
from models.superheros import Superheros


# - API Endpoint ----------------------------------------------#
#   This is the search endpoint                                #
# -------------------------------------------------------------#
@app.route('/superhero', methods=['POST'])
def search_superhero():
    app.logger.info('SEARCH SUPERHERO')
    if request.method == 'POST':
        superhero = request.json.get('superhero')
        if superhero:
            result = Superheros.query.filter(Superheros.name == superhero).first()
            if result:
                return Response('"message": "success",'
                                '"superhero": {"name": ' + result.name + '}',
                                status=200,
                                mimetype='application/json')
            else:
                return Response('"message": "No Hero Found"',
                                status=200,
                                mimetype='application/json')
    return Response('"message": "Something went wrong"',
                    status=500,
                    mimetype='application/json')

