from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
io = SocketIO(app)

@app.route("/")
def chat():
    return render_template("Escrita.html")

@io.on('sendMessage') 
def send_message(msg):
    emit('getMessage', msg, broadcast=True)  # Adicionado broadcast=True para enviar a todos os clientes

if __name__ == "__main__":
    io.run(app, debug=True)
