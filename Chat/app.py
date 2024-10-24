from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("Escrita.html")

# Recebe o conteúdo atualizado da div e envia para todos os clientes conectados
@socketio.on('updateContent')
def update_content(data):
    emit('receiveUpdate', data, broadcast=True)  # Transmite o novo conteúdo para todos

if __name__ == "__main__":
    socketio.run(app, debug=True)
