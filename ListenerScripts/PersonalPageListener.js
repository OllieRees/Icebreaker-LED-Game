/** Attached to the personal page. Includes a method that receives data from the server and sends messages to the server.
 * The two methods are independent of each other. */

showQuestionAnswerer = function(dragonServerAddress, scoreFieldID, questionFieldID, answererFieldID) {
    let data = JSON.parse(pollServer(dragonServerAddress)); //called every time the server sends a message
    var vals;
    for (vals in data.split(",")) {
        if (vals.contains("current score")) {document.getElementById(scoreFieldID).value = vals.split(":")}
        if (vals.contains("question")) {document.getElementById(questionFieldID).value = vals.split(":")}
        if (vals.contains("answerer")) {document.getElementById(answererFieldID).value = vals.split(":")}
    }
};

/** Sends the answer to the DragonServer */
sendAnswer = function(dragonServerAddress, answerFieldID) {
    let conn = new WebSocket(dragonServerAddress + ":63636");
    let answer = document.getElementById(answerFieldID).value;
    conn.onopen = function(){
        conn.send("answer:" + answer);
    };
};
