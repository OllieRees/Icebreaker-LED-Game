/** Whenever the DragonServer sends a message to the webapp, return the data from the message. */
pollServer = function(dragonServerAddress) {
    let conn = new WebSocket(dragonServerAddress + ":63636");

    //just return the message sent by the server
    conn.onmessage = function (e) {
        let data = e.data; //just to be safe
        conn.close();
        return data;
    }
};
