import json

from flask import Response, request
from app import app, db
from models.superheros import Superheros
from models.favourites import Favourites


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
                return Response('{"message": "success",'
                                '"superhero": {"name": "' + result.name + '", "id": "' + str(result.id) + '"}}',
                                status=200,
                                mimetype='application/json')
            else:
                return Response('{"message": "No Hero Found"}',
                                status=200,
                                mimetype='application/json')
    return Response('"message": "Something went wrong"',
                    status=500,
                    mimetype='application/json')


# - API Endpoint ----------------------------------------------#
#   This is the init endpoint                                  #
# -------------------------------------------------------------#
@app.route('/init', methods=['GET'])
def init_superhero():
    app.logger.info('INIT SUPERHEROS')
    if Superheros.query.count() == 0:
        db.session.add_all([Superheros(name='batman'),
                            Superheros(name='superman'),
                            Superheros(name='spiderman')])
        db.session.commit()
        return Response('"message": "Populated!",',
                        status=200,
                        mimetype='application/json')
    else:
        return Response('"message": "Already populated",',
                        status=200,
                        mimetype='application/json')

    return Response('"message": "Something went wrong"',
                    status=500,
                    mimetype='application/json')


# - API Endpoint ----------------------------------------------#
#   This is the favourite endpoint                             #
# -------------------------------------------------------------#
@app.route('/favourite', methods=['POST'])
def favourite_superhero():
    app.logger.info('FAVOURITE')
    if request.method == 'POST':
        id = request.json.get('id')
        if id:
            favourite = Favourites(superhero_id=id)
            db.session.add(favourite)
            db.session.commit()
            return Response('{"message": "success"}',
                            status=200,
                            mimetype='application/json')

    return Response('{"message": "Something went wrong"}',
                    status=500,
                    mimetype='application/json')


# - API Endpoint ----------------------------------------------#
#   This is the get favourite endpoint                         #
# -------------------------------------------------------------#
@app.route('/get_favourite', methods=['GET'])
def get_favourite_superhero():
    app.logger.info('GET FAVOURITE')
    if request.method == 'GET':
        data = Favourites.query.all()
        return Response('{"favourites": "' + str(data) + '"}',
                        status=200,
                        mimetype='application/json')
    return Response('{"message": "Something went wrong"}',
                    status=500,
                    mimetype='application/json')
