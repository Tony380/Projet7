from flask import render_template, request
from app.program.parser import Parser
from app.program.gmap import Gmap
from app.program.wiki import Wiki
from app import app

app.config.from_object('config')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api')
def get_response():
    user_text = request.args.get("question")

    response = Parser(user_text).parser()

    gmap = Gmap(response).search()

    wiki = Wiki(response).search()

    if gmap == 'no result found' or wiki == 'no result found':
        answer = {'result': 'no result found'}
        return answer

    else:
        answer = {'adress': gmap['adress'],
                  'lat': gmap['lat'],
                  'lng': gmap['lng'],
                  'page': wiki['page'],
                  'url': wiki['url']}

        return answer
