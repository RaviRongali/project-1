import socket
import select


def seed(ip, port):
    # s = socket.socket()
    print(f"Socket successfully created where ip= {ip} port= {port}")
    # s.bind((ip, port))
    # s.listen(5)
    ds = (ip, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ds)
    server.listen(1)

    return server
    # servers.append(server)
    # while True:
    #     print(ML)
    #     # Establish connection with client.
    #     c, addr = s.accept()
    #     ML.append(addr)
    #     print("Got connection from", addr)
    #     # send a thank you message to the client.
    #     c.send(bytes("Thank you for connecting", "utf-8"))
    #     # Close the connection with the client
    #     c.close()


def k(servers):

    # for port in portlist:

    while True:
        # Wait for any of the listening servers to get a client
        # connection attempt
        readable, _, _ = select.select(servers, [], [])
        ready_server = readable[0]
        c, address = ready_server.accept()
        # addr = s.accept()
        # ML.append(address)
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