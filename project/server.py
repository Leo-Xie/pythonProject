"This is a class to build a server"
import icns
import sys, os


num = raw_input('Please input the port you want to open : ')

myserver = icns.Network(int(num))

print "The server is built on port %s, waiting for connection..." % (num)

def main():
	"This is a function to operate a server"
	temp = raw_input('----------------------------------------\nInput [1] to add a client and communicate\nInput [2] to close the server\n----------------------------------------\n')
	if temp == '1': 
		addr = raw_input('Please input client ip address: ')
		cport = raw_input('Plese input client port: ')
		n = myserver.add_neighbour(addr, int(cport))
		while True:
			source, message = myserver.receive()
			reply  = "Hello: "+source
			print reply
			myserver.send(n,reply)
	elif temp == '2':
		os._exit(0)
	elif temp == '3':
		source, message = myserver.receive()
		
	else:
		print 'error input'
		main()

main()








