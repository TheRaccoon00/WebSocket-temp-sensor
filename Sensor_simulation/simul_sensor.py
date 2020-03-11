from flask_socketio import SocketIO,emit
import socketio
import time
import random

sensor = socketio.Client()
sensor.connect('http://localhost:5000', namespaces=['/sensor'])

while 1:
    sensor.emit('my event', {"temp":random.randint(-50,50),"time":time.time()}, namespace='/sensor')
    time.sleep(10)

sensor.disconnect()
