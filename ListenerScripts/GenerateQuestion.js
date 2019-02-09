/** Get Question from DragonServer and format it to HTML document */

/** Get question from DragonServer and format it for  */
getServerData = function(dragonServerAddress) {
    let data = pollServer(dragonServerAddress); //question from DragonServer
    let msg = JSON.parse(data); //turn JSON msg to an object

};

/**  Write question to HTML document with the formatted question */
writeQuestion = function(dragonServerAddress) {
    let question = getQuestion(getServerData(dragonServerAddress));
    document.getElementById("icebreaker-question").innerHTML = question;
};

/** Format the DragonServer message to just be the string */
getQuestion = function(serverMsg) {
    let questions = serverMsg.question; //make this a global var.?
    return questions[Math.floor(Math.random()) * questions.length];
};
