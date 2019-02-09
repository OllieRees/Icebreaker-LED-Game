from flask import Flask, render_template, request, make_response
import threading
import random
from websocketComms import websocketComms
from gameLogic import iceBreaker

app = Flask(__name__)
ws = websocketComms()
USERS = set()
ib = iceBreaker(USERS)

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
        for line in file:
            questionList += line.strip()
    
    filteredQuestionList = []
    for i in random.sample(range(len(questionList)), 6):
        filteredQuestionList += questionList[i]

    finalQuestionList = {}

    resp = make_response(render_template("questions.html", questions=finalQuestionList))
    resp.setCookie('name', name)
    return resp

@app.route('/game', methods = ['POST', 'GET'])
def game():
    ib.play()

if __name__ == '__main__':
    ws.start()
    app.run(debug=True, host='127.0.0.1', port=8080)