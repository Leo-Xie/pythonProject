import icns
import sys, os

num = raw_input('Please input the port: ')

myclient = icns.Network(int(num))

addr = raw_input('Please input server ip address: ')
svport = raw_input('Please input server port: ')

n = myclient.add_neighbour(addr, int(svport))

x = icns.UI("Client")

going = True
fd = x.getfd()
while going:
    line = os.read(fd, 100)
    if line == '/q':
        going = False
    else:
    	myclient.send(n,line)
    	reply, message = myclient.receive()
        x.addline("you said: " +line+" \nreply: "+reply)
x.stop()
