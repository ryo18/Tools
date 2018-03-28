#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# clean the screen
subprocess.call('clear',shell=True)

# input
remoteServer = raw_input('Enter a remote host to scan: ')
remoteServerIP = socket.gethostbyname(remoteServer)

# banner
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServer,port))
		if result == 0:
			print "PORT {}:		Open! ".format(port)
		sock.close()
except KeyboardInterrupt:
	print "You pressed Ctrl+C"
	sys.exit() 
except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit() 
except socket.error:
	print "Couldn't connect to server"
	sys.exit()

# check the time again
t2 = datetime.now()

# calculates time 
total = t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
