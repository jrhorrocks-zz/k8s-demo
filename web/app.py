from flask import Flask, render_template, request

import socket

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("hello.html", name=socket.gethostname(), ip=socket.gethostbyname(socket.gethostname()))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
