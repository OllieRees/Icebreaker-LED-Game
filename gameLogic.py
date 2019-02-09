import threading
import json

class iceBreaker():

    def __init__(self):
        self.users = list()
        self.questions = dict()

    def resetGame(self):
        self.users = list()
        self.questions = dict()

    def addUser(self, name):
        self.users.append(name)

    def setActive(self, name):
        pass

    def requestQuestion(self):
        pass

    def checkAnswer(self, question, answer):
        pass

    def setQuestions(self, questionList):
        self.questions = questionList

    def play(self):
        pass

    def processMessage(self, message):
        data = json.loads(message)
        return ""      