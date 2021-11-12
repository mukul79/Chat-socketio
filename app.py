from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    uname = request.args.get('username')
    return render_template('index2.html',username = uname)

# @socketio.on('connect')
# def test_connect(auth):
#     print('connected')

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('my event')
def handle_message(data):
    print(data['data'])

@socketio.on('join_room')
def handle_message(data):
    print('sgjdsdg')

if __name__ == '__main__':
    socketio.run(app)