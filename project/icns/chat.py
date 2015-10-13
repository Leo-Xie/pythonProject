number = int(sys.argv[1])
neighbour = sys.argv[2].split(":")
message = " ".join(sys.argv[3:])

n1 = icns.Network(number)
n = n1.add_neighbour(neighbour[0], int(neighbour[1]))

n1.send(n, message)

