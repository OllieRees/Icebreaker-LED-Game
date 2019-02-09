import threading

class iceBreaker():

    def __init__(self):
        self.users = []
        self.questions = {}

    def addUser(self, name):
        self.users += name

    def checkAnswer(self, question, answer):
        pass

    def setQuestions(self, questionList):
        self.questions = questionList

    def play(self):
        pass