from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
io = SocketIO(app)

messages = []
clients = set()  # Conjunto para armazenar os clientes conectados

@app.route('/')
def home():
    return render_template("index.html")

@io.on('connect')
def connect_handler():
    global clients
    clients.add(threading.current_thread())  # Adiciona a thread atual à lista de clientes

@io.on('disconnect')
def disconnect_handler():
    global clients
    clients.remove(threading.current_thread())  # Remove a thread atual da lista de clientes


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


def handle_client(client_thread):
    # Aqui você pode realizar ações específicas para um cliente,
    # como enviar e receber mensagens específicas para esse cliente.
    pass


def run_flask_app():
    io.run(app)


