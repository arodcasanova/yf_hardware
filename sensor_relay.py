#!/usr/bin/env python

from socketIO_client import SocketIO, LoggingNamespace

action = {'type': 'SET_SENSOR_STATES', 'sensors': ['1', '2', '3']}

socket = SocketIO('http://yf-server.herokuapp.com', 80, LoggingNamespace)
socket.emit('action', action)
socket.wait(seconds=1)