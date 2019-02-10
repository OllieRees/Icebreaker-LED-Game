/** Attached to the personal page. Includes a method that receives data from the server and sends messages to the server.
 * The two methods are independent of each other. */

PersonalPageListener = function(dragonServerAddress) {
    conn = new WebSocket(dragonServerAddress + ":63636");

    /** Send action, question and answer data when user submits answer*/
    button.onClick = function(event) {
        let name = document.cookie.split("=")[1];
        conn.send("action:answer,question:" + document.getElementById(textbox1).value + ",answer:" + document.getElementById(textbox3).value
            + ",user:" + name);
    };
    conn.onmessage = function(e) {
        for (data in e.data.split(",")) {
            if (data.contains("current score")) {
                document.getElementById(textbox4).value = data.split(":")[1];
                continue;
            }
            if(data.contains("question")) {
                document.getElementById(textbox1).value = data.split(":")[1];
                continue;
            }
            if(data .contains("answerer")) {
                document.getElementById(textbox2).value = data.split(":")[1];
            }
        }
    };
};


