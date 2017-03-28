#!/usr/bin/env python

from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('http://yf-server.herokuapp.com', 80, LoggingNamespace) as socketIO:
    socketIO.emit('action', {'type': 'SET_SENSOR_STATES', 'sensors': ['Louie', 'Gia', 'Jimmy']})
    socketIO.wait(seconds=1)