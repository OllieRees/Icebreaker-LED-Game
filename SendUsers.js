/** Gets the username from the web app and sends it to the dragon server */

//gets the username string from a textfield on the html page.
getUsername = function(TextFieldID) {
    return document.getElementById(TextFieldID).value;
};

//Sends a username to the dragon server over port 6363.
sendUsername = function(username, dragonServerAddress) {
    let conn = new WebSocket(dragonServerAddress + ":6363");
    conn.onopen = function() {
        conn.send("Username : " + username);
    };
};
