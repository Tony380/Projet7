"""Views file will send answer to front-end"""
from flask import render_template, request, jsonify
from app.program.parser import Parser
from app.program.gmap import Gmap
from app.program.wiki import Wiki
from app.program.sentences import sentence
from app import app

# for API key
app.config.from_object('config')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api')
def get_response():
    """Response to front-end"""
    user_text = request.args.get("question")

    response = Parser(user_text).parser()

    gmap = Gmap(response).search()

    # random sentences
    sentences = sentence()

    if gmap == 'no result found':
        answer = {'result': 'no result found',
                  'res': sentences['res']}
        return jsonify(answer)

    else:
        wiki = Wiki(response, gmap['lat'], gmap['lng']).search()

        if wiki == 'no result found':
            answer = {'result': 'no result found',
                      'res': sentences['res']}
            return jsonify(answer)

        else:
            answer = {'adress': gmap['adress'],
                      'lat': gmap['lat'],
                      'lng': gmap['lng'],
                      'page': wiki['page'],
                      'url': wiki['url'],
                      'adr': sentences['adr'],
                      'wik': sentences['wik']}

            return jsonify(answer)
