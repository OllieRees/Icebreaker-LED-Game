/** Creates a cookie for the game on the user's phone */
/** Will be called in the login page */

/** Create a webapp cookie with the username */
createWebAppCookie = function(TextFieldID) {
    let username = getUsername(TextFieldID);
    document.cookie = "username=" + username;
};