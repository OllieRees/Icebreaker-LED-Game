/** Gets the answer for each question */

/** Gets the answer from the textfield */
getAnswer = function(TextFieldID) {
    return document.getElementById(TextFieldID).value;
};

/** Sends the answer inputted to the DragonServer */
sendAnswer = function(TextFieldID, dragonServerAddress) {
    let answer = getAnswer(TextFieldID);
    let conn = new WebSocket(dragonServerAddress + ":6363");
    conn.onopen = function() {
        conn.send("Answer : " + answer);
    };
};
