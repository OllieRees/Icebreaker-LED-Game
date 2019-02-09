/** Gets the username from the web app and sends it to the dragon server */

//gets the username string from a textfield on the html page.
getUsername = function(TextFieldID) {
    return document.getElementById(TextFieldID).value;
};

//Sends a username to the dragon server over port 6363. Attached to a submit button on the login page.
sendUsername = function(TextFieldID, dragonServerAddress) {
    let username = getUsername(TextFieldID);
    let conn = new WebSocket(dragonServerAddress + ":63636");
    conn.onopen = function() {
        conn.send("Username : " + username);
    };
};

