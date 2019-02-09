/** Sends the answer for each question to the DragonServer */

/** Gets the answer from the textfield */
getAnswer = function(TextFieldID) {
    return document.getElementById(TextFieldID).value;
};

/** Get game cookie w/ username */
getCookie = function() {
    return document.cookie;
};

/** Get username of answerer */
getAnswererName = function() {
  let decodedCookie = decodeURIComponent(getCookie()); //might change the getCookie method
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
    let conn = new WebSocket("ws://" + dragonServerAddress + ":63636/");
    conn.onopen = function() {
        conn.send("Username : " + username + ", Answer : " + answer);
    };
};