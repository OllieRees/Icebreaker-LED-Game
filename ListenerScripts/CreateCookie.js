/** Creates a cookie for the game on the user's phone */
/** Will be called in the login page */
/** Deprecated */

/** Create a webapp cookie with the username */
createWebAppCookie = function(TextFieldID) {
    let username = document.getElementById(TextFieldID).value;
    document.cookie = "username=" + username;
};