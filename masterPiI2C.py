import smbus
import time

bus = smbus.SMBus(1)
arduinos = []

def setupArduinos(number):
	addr1 = 0x04
	for i in range(0, number):
		arduinos.append(addr1 + i)
	return -1

def pingSlave(address):
	bus.write_byte(address, 1)
	return -1

def readSlave(address):
	data = bus.read_byte(address)
	return data



numArduinos = 1 #change when add more arduinos	
setupArduinos(numArduinos)

while True:
	sensorData = {}
	for slaveAddr in arduinos:
		pingSlave(slaveAddr)
		time.sleep(.2)
		slaveData = readSlave(slaveAddr)
		sensorData[slaveAddr] = slaveData
	print sensorData

