from flask import Flask, request, render_template, Config
from flask_socketio import SocketIO,emit

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import time
import os

from models import *

# Flask routes
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@localhost/myDbName"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

socketio = SocketIO(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@socketio.on('my event', namespace='/sensor')
def test_message(message):
    r = Readings(temperature=message['temp'],time=message["time"])
    db.session.add(r)
    db.session.commit()
    emit('my response', {'temp': message['temp'],'time':message["time"]}, broadcast=True)

@socketio.on('connect', namespace='/sensor')
def test_connect():
    readings = Readings.query.all()
    ret = []
    for reading in readings:
        ret.append({"temp":reading.temperature,"time":reading.time})
    emit('connected', {'data': ret})

@socketio.on('disconnect', namespace='/sensor')
def test_disconnect():
    print('Sensor disconnected')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app,host='localhost')
