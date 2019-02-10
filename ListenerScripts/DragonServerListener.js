/** Whenever the DragonServer sends a message to the webapp, print out the message */
pollServer = function(dragonServerAddress) {
    let conn = new WebSocket(dragonServerAddress + ":6363");

    //just return the message sent by the server
    conn.onmessage = function (e) {
        let data = e.data; //just to be safe
        conn.close();
        return data;
    }
};

/** Receives the value from the DragonServer's message */
receiveValue = function(dragonServerAddress) {
    var data = JSON.parse(pollServer(dragonServerAddress)); //might not need to parse it
    let value = data.split(":")[1]; //takes the value of the data
    return(value);
};
