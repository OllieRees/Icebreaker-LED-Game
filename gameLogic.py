import threading
import json
import random

class iceBreaker():

    def __init__(self):
        self.users = list() #just a list of users
        self.questions = dict() #key is the user name, and the value is a dict of question:answer. 
        self.activeUser = ""

    def resetGame(self):
        self.users = list()
        self.questions = dict()
        self.activeUser = ""

    def addUser(self, name, questions):
        self.users.append(name) 
        self.questions.update({name : questions}) #add user to questions

    #Assign a activeUser 
    def setActive(self, name):
        self.activeUser = name 

    #Request a question to send. Picks from the questions dict excluding the key-val pair with the activeuser as key 
    def requestQuestion(self):
        possibleQuestions = [for key, value in self.questions.getitems() if key not activeUser] #reduces questions to possible questions
        randomUser = random.choice(possibleQuestions.keys()) #gets a random user
        askedQuestion = random.choice(list(randomUser)) #gets a random question/key from randomUser
        return askedQuestion
        
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
        data = json.loads(message)
        return ""      