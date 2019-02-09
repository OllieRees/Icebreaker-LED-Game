/* Generate random question from the list provided by the users */

    /* Include properties like who asks the question */

    /* Takes a list of questions and picks one out at random */
getQuestion = function(listOfQuestions) {
    question = listOfQuestions[Math.floor(Math.random() * items.length)];
    return question;
    //make sure that one question isn't repeated multiple times for a unique pair of asker-answer player
};

/* Determine who the question should be asked to */
askWho = function(usernameAsker) {
    //get list of users
    //take away usernameAsker from the list LOCALLY
    //get a random user from the new list
};



    /* How would I print the question out and who to ask? */