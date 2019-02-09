from flask import Flask, render_template
import threading
import random
from websocketComms import websocketComms
from gameLogic import iceBreaker

app = Flask(__name__)
ws = websocketComms()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/questions', methods = ['POST', 'GET'])
def questions():
    questionList = []
    with open("static/questions.txt") as file:
        for line in file:
            questionList += line.strip()
    
    newQuestionList = []
    for i in random.sample(range(len(questionList)), 6):
        newQuestionList += questionList[i]

    newNewQuestionList = zip(range(len(newQuestionList)), newQuestionList)
    return render_template("questions.html", questions=newNewQuestionList)

@app.route('/game', methods = ['POST', 'GET'])
def game():
    iceBreaker().play()

if __name__ == '__main__':
    ws.start()
    app.run(debug=True, host='127.0.0.1', port=8080)