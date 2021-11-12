from flask import Flask, render_template,request
from flask_socketio import SocketIO,join_room, leave_room,send, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/chat', methods = ['GET','POST'])
def chat():
    name1 = request.form.get("Name") 
    return render_template('chat.html', name = name1)

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data['data'])

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)

if __name__ == '__main__':
    socketio.run(app)