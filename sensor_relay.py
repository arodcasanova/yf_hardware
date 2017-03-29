#!/usr/bin/env python

from datetime import datetime
from socketIO_client import SocketIO, LoggingNamespace

socket = SocketIO('http://yf-server.herokuapp.com', 80, LoggingNamespace)
action = {'type': 'SET_SENSOR_STATES', 'sensors': ['ay', 'ay']}
socket.emit('action', action)

# while True:
# 	time = datetime.now().strftime("%I:%M:%f")
# 	action = {'type': 'SET_SENSOR_STATES', 'sensors': ['sensor1  ' + time, 'sensor2  ' + time, 'sensor3  ' + time]}
# 	socket.emit('action', action)
	



