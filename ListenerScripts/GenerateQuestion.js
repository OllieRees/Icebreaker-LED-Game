/** Get Question from DragonServer and format it to HTML document */

/** Get question from DragonServer and format it for  */
getQuestion = function(dragonServerAddress) {
    let data = pollServer(dragonServerAddress); //question from DragonServer
    let msg = JSON.parse(data); //get JSON format of DragonServer's message

};

/**  Write question to HTML document with the formatted question */
writeQuestion = function() {

};

/** Format the DragonServer message to just be the string */
formatServerData = function(serverMsg) {

};