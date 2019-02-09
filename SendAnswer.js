/** Gets the answer for each question */

/** Gets the answer from the textfield */
getAnswer = function(TextFieldID) {
    return document.getElementById(TextFieldID).value;
};

/** Get username of answerer */
getAnswererName = function() {
  let decodedCookie = decodeURIComponent(document.cookie);
  let cookieFields = decodedCookie.split(";");
  let username = ""; //default username
  for (let fields in cookieFields) {
      if (fields.contains("username")) {
          username = fields.split(":")[1]; //remove username tag
          username = username.substr(1, username.length); //remove any spaces at the beginning
      }
  }
  return username;
};

/** Sends the answer inputted to the DragonServer */
sendAnswer = function(TextFieldID, dragonServerAddress) {
    let answer = getAnswer(TextFieldID);
    let username = getAnswererName();
    let conn = new WebSocket(dragonServerAddress + ":6363");
    conn.onopen = function() {
        conn.send("Username : " + username + ", Answer : " + answer);
    };
};

