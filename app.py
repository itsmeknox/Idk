from flask import Flask, render_template_string
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Hello world"

@app.route('/socket')
def socket():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>SocketIO Test</title>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
            <script type="text/javascript" charset="utf-8">
                document.addEventListener('DOMContentLoaded', function() {
                    var socket = io.connect('http://' + document.domain + ':' + location.port);
                    socket.on('connect', function() {
                        console.log('Connected to server');
                        socket.send('Hello Server!');
                    });
                    socket.on('message', function(msg) {
                        console.log('Received message: ' + msg);
                    });
                });
            </script>
        </head>
        <body>
            <h1>SocketIO Test</h1>
        </body>
        </html>
    ''')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
        
if __name__ == '__main__':
    print("Running the app")
    app.run(debug=False, host="0.0.0.0", port=5000)