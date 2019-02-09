import threading
import random

class iceBreaker():

    def __init__(self):
        self.users = list() #just a list of users
        self.questions = dict() #key is the user name, and the value is a dict of question:answer. 

    def resetGame(self):
        self.users = list()
        self.questions = dict()

    def addUser(self, name, questions):
        self.users.append(name)
        self.questions.update({name : questions}) #add user to questions

    def setActive(self, name):
        pass

    #Request a question to send
    def requestQuestion(self):
        self.question = random.choice(self.questions)
        #send question to be sent as HTML label

    #check if the answer given is the same as the answer in the question-answer hashmap
    def checkAnswer(self, question, answer):
        questionAnswer = self.questions.get(activeUser) #gets the question and answer dict for the activeUser
        if (answer == questionAnswer.get(question)): #check if the answer provided is the same as the one in the questions dict
            return True
        else:
            return False

    def setQuestions(self, questionList):
        self.questions = questionList

    def play(self):
        pass

    def processMessage(self, message):
        return ""        