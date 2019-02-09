/** Whenever the DragonServer sends a message to the webapp, print out the message */
pollServer = function(dragonServerAddress) {
    let conn = new WebSocket(dragonServerAddress + ":6363");

    //just print out the message sent by the server
    conn.onmessage = function (e) {
        let data = e.data; //just to be safe
        conn.close();
        return data;
    }
};