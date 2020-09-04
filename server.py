import socket
import select


class MySocket:
    """demonstration class only
    - coded for clarity, not efficiency
    """

    def __init__(self, sock=None, data=None):
        if sock is None:
            self.data = []
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        else:
            self.data = data
            self.sock = sock

    def connect(self, host, port):
        ds = (host, port)
        self.sock.bind(ds)
        self.sock.listen(1)

    def adduser(self, address):
        self.data.append(address)
        return self.data

    # def mysend(self, msg):
    #     totalsent = 0
    #     while totalsent < MSGLEN:
    #         sent = self.sock.send(msg[totalsent:])
    #         if sent == 0:
    #             raise RuntimeError("socket connection broken")
    #         totalsent = totalsent + sent

    # def myreceive(self):
    #     chunks = []
    #     bytes_recd = 0
    #     while bytes_recd < MSGLEN:
    #         chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
    #         if chunk == b"":
    #             raise RuntimeError("socket connection broken")
    #         chunks.append(chunk)
    #         bytes_recd = bytes_recd + len(chunk)
    #     return b"".join(chunks)


def seed(ip, port):
    # s = socket.socket()

    # s.bind((ip, port))
    # s.listen(5)
    server = MySocket()
    server.connect(ip, port)
    print(f"Socket successfully created where ip= {ip} port= {port}")
    return server


def k(servers):

    # for port in portlist:

    while True:
        # Wait for any of the listening servers to get a client
        # connection attempt
        s1 = []
        s2 = []
        for server in servers:
            s1.append(server.sock)
            s2.append(server.data)
        readable, _, _ = select.select(s1, [], [])
        ready_server = readable[0]
        i = s1.index(ready_server)
        c, address = ready_server.accept()
        sockk = MySocket(ready_server, s2[i])
        list = sockk.adduser(address)
        print(list)
        print("Got connection from", address)
        # send a thank you message to the client.
        c.send(bytes("Thank you for connecting", "utf-8"))
        # Close the connection with the client
        c.close()


def preprocess():
    fh = open("config.txt")
    lines = fh.readlines()
    servers = []
    for line in lines:
        ip = line.split(":")[0]
        port = line.split(":")[1]
        print("ip= ", ip, "port= ", port)
        server = seed(ip, int(port))
        servers.append(server)
    k(servers)

    fh.close()


preprocess()


##to check if multiple seeds running check using cmd $netstat -tulpn
#