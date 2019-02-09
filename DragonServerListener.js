/** Whenever the DragonServer sends a message to the webapp, print out the message */
pollServer = function(dragonServerAddress) {
    conn = new WebSocket(dragonServerAddress + ":6363");

    //just print out the message sent by the server
    conn.onmessage = function (e) {
        Console.log(e.data);
    }
};