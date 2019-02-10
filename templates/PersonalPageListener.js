/** Attached to the personal page. Includes a method that receives data from the server and sends messages to the server.
 * The two methods are independent of each other. */

receiveQuestion = function() {
    let data = JSON.parse(pollServer());
    if (data.contains("question")) {
        return data.split(":")[1];
    }
};

/** This will probably be changed : it's shit. */
receiveAnswerer = function() {
    let data = JSON.parse(pollServer()); //can't we just use receiveData()?
    if (data.contains("answerer")) {
        return data.split(":")[1];
    }
};

/** Sends the answer to the DragonServer */
sendAnswer = function(dragonServerAddress, answerFieldID) {
    let conn = new WebSocket(dragonServerAddress + ":6363");
    let answer = document.getElementById(answerFieldID).value;
    conn.onopen = function(){
        conn.send("answer:" + answer);
    };
};
