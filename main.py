from flask import Flask, render_template, request, make_response
import threading
import random
from websocketComms import websocketComms
from gameLogic import iceBreaker

app = Flask(__name__)
ws = websocketComms()
USERS = set()
ib = iceBreaker()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/questions', methods = ['POST', 'GET'])
def questions():
    name = "default"
    if request.method == 'POST': 
        name = request.form['name']
    questionList = []

    with open("static/questions.txt") as file:
        questionList = [line.rstrip() for line in file]

    filteredQuestionList = []
    for i in random.sample(range(len(questionList)), 6):
        filteredQuestionList.append(questionList[i])

    resp = make_response(render_template(
        "questions.html", 
        questions=filteredQuestionList,
        numOfQs=len(filteredQuestionList)
        ))
    resp.set_cookie('name', name)
    return resp

@app.route('/game', methods = ['POST', 'GET'])
def game():
    return render_template("personal.html")

if __name__ == '__main__':
    ws.start()
    app.run(debug=True, host='127.0.0.1', port=8080)