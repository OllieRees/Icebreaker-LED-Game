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
        possibleQuestions = dict(self.questions)
        possibleQuestions.pop(self.activeUser) #reduces questions to possible questions
        randomUser = random.choice(list(possibleQuestions.keys())) #gets a random user
        askedQuestion = random.choice(list(possibleQuestions.get(randomUser).keys())) #gets a random question/key from randomUser
        return [randomUser,askedQuestion]
        
        #send question to be sent as HTML label

    #check if the answer given is the same as the answer in the question-answer hashmap
    def checkAnswer(self, question, answer, user):
        questionAnswer = self.questions.get(user) #gets the question and answer dict for the activeUser
        return answer == questionAnswer.get(question) #check if the answer provided is the same as the one in the questions dict

    #set questions at the beginning
    def setQuestions(self, questionList):
        self.questions = questionList

    #would be the game thread - but may use states to run the game
    def play(self):
        pass

    #process http message? Probably not.
    def processMessage(self, message):
        data = message.split(',')
        if data[0].split(':')[1] == 'answer':
            if self.checkAnswer(data[1].split(':')[1], data[2].split(':')[1], data[3].split(':')[1]):
                return ["client", "success"]
        return ["", ""]   

if __name__ == "__main__":
    ib = iceBreaker()

    dicts = [
        {"a":"A", "b":"B"},
        {"c":"C", "d":"D"},
        {"e":"E", "f":"F"},
        {"g":"G", "h":"H"},
        {"i":"I", "j":"J"}
    ]
    users = [
        'test1',
        'test2',
        'test3',
        'test4',
        'test5',
    ]

    for i in range(5):
        ib.addUser(users[i], dicts[i])
    
    i = 0
    while True:
        i = i+1 if i <= 3 else 0
        ib.setActive(users[i])
        q = ib.requestQuestion()
        user = q[0]
        question = q[1]
        print(user, ':', question)
        print(ib.checkAnswer(question, input(), user))
