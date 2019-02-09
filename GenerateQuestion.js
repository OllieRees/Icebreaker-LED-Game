/** Generate random question from the list provided by the users: determines the question, who's asked and who says it. Passes it on to the website of the user */
/** Class is activated when time limit for previous question runs out, or previous question is successfully answered */

class GenerateQuestion {
    /** Include properties like who asks the question */
    userAsks; //who asks the question
    userAnswer; //who answers the question

    /** Takes a list of questions and picks one out at random */
    getQuestion = function (listOfQuestions) {
        question = listOfQuestions[Math.floor(Math.random() * listOfQuestions.length)];
        return question;
        //make sure that one question isn't repeated multiple times for a unique pair of asker-answer player
    };

    /** Determine who the question should be asked to */
    answerWho = function () {
        //get list of users
        possibleUsers = getUsers() - userAskers;
        //take away usernameAsker from the list LOCALLY
        //get a random user from the new list
        answerer =  possibleUsers[Math.floor(Math.random() * possibleUsers.length)];
        return answerer;
    }

    /* How would I print the question out and who to ask? */

}
