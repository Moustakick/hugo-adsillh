#!/usr/bin/python3
import os
import sys
import socket

def main():
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print ("Wrong arguments")
        sys.exit(os.EX_USAGE)

    link = sys.argv[1]

    print("Arguments OK")

    ip = socket.getaddrinfo(sys.argv[1],"http",0,socket.SOCK_STREAM)

# unpack ipv6 tuple
    (family, type, proto, canonname, sockaddr) = ip[0]

    sock = socket.socket(family,type,proto)

    sock.connect(sockaddr)








if __name__ == "__main__":
    main()
