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
    question = Parser(user_text)
    response = question.parser()
    gmap = Gmap()
    gmap.search(response)
    wiki = Wiki()
    wiki.search(response)
    answer = {'coords': gmap.location, 'page': wiki.page, 'url': wiki.url}
    return answer
