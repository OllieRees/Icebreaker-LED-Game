# Ice Breaker
## Web app game for Hack the South 2019

### A web app which is a conversation starter, icebreaker and a game all in one! Nothing more than a web browser needed!

### Inspiration
- We wanted to build something that incorporated networking and scripting
- We were inspired by AmEx's proposition to make an something to break the ice.

### What it does
A Web app that anyone with a web browser can participate in. You answer a few randomly chosen questions before starting, 
then everyone involved is randomly assigned questions that they can only answer by talking to the other players. 
Answer enough questions correctly **as a team** to win.

### How we built it
- **HTML5, CSS, JavaScript** for front end.
- **DragonBoard** for hosting a web server.
- **Flask** (a python module) for web hosting, enabling us to also use python for the raw game logic.
- **The WebSockets API** for two-way communication between the server and the client to enable in-place live updating of 
web pages with javascript used for the client side.

### Challenges we ran into
Before starting we didn't know javascript, Flask, or websockets so we have had to learn these new technologies very 
quickly before being able to produce anything.

### Accomplishments that we're proud of
We created a web app in 24 hours!

### What we learned
Learning many new technologies at once it quite a challenge, and possibly not a good choice for a 
hackathon where time is limited. 

### What's next for Ice Breaker
More features, more interactions, more robust playability, scalability, reconnecting users.

## To run
Dependencies:
- Python 3
- Python modules: flask, websockets

Run the main.py file. Connect to the machine now running the webserver on port 8080.
