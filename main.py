from flask import Flask, render_template
import threading
from websocketComms import websocketComms

app = Flask(__name__)
ws = websocketComms()

@app.route('/')
def index():
    return render_template("Icebreaker-LED-Game/index.html")
    # return "Hello world"

@app.route('/questions')
def questions():
    questionList = []
    with open("static/questions.txt") as file:
        for line in file:
            questionList += line.strip()
    return render_template("Icebreaker-LED-Game/questions.html", question=questionList[0])

if __name__ == '__main__':
    ws.start()
    app.run(debug=True, host='127.0.0.1', port=8080)