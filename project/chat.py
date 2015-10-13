"This class is used to build a chat connection from different ip address"

import thread
import time
import icns
import sys, os


number = raw_input('Please input your number: \n')
chatnode = icns.Network(int(number))
addr = raw_input('Please input target ip address: \n')
svport = raw_input('Please input target number: \n')
n = chatnode.add_neighbour(addr, int(svport))

x = icns.UI('Welcome! You are now talking with IP: '+addr+ ' ,type /q to quit the chat')
going = True
fd = x.getfd()

def chat( threadName, delay):
	"This fucntion is used to send and receive message."
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		if threadName == "Thread-1":
			line = os.read(fd, 100)
			if line == '/q':
				going = False
				x.stop()
				os._exit(0)
			else:
				x.addline("you said: " +line)
				chatnode.send(n, line) 
		else:		
			message, source = chatnode.receive()
			x.addline(addr +" " +"says: " +message)
			

try:
   thread.start_new_thread( chat, ("Thread-1", 1, ) )
   thread.start_new_thread( chat, ("Thread-2", 1, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass




