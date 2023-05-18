from flask.app import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
io = SocketIO(app)

messages = []


@app.route('/')
def home():
    return render_template("index.html")


@io.on('sendMessage')
def send_message_handler(msg):
    global messages
    if len(messages) > 10:
        messages = messages[1:]
        messages.append(msg)
    else:
        messages.append(msg)
    emit('getMessage', msg, broadcast=True)


@io.on('message')
def message_handler(msg):
    send(messages)

