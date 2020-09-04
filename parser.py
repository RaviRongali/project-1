fh = open("config.txt")
lines = fh.readlines()
for line in lines:
    ip = line.split(":")[0]
    port = line.split(":")[1]
    print("ip= ", ip, "port= ", port)
fh.close()