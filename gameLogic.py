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

    #set a user active to call requestQuestion for the user
    def setActive(self, name):
        return questions.get(name) 

    #Request a question to send
    def requestQuestion(self):
        self.question = random.choice(self.questions)
        #send question to be sent as HTML label

    #check if the answer given is the same as the answer in the question-answer hashmap
    def checkAnswer(self, question, answer):
        questionAnswer = self.questions.get(activeUser) #gets the question and answer dict for the activeUser
        return (answer == questionAnswer.get(question)): #check if the answer provided is the same as the one in the questions dict

    #set questions at the beginning
    def setQuestions(self, questionList):
        self.questions = questionList

    #would be the game thread - but may use states to run the game
    def play(self):
        pass

    #process http message? Probably not.
    def processMessage(self, message):
        return ""        