#!/usr/bin/python3
import socket
import select
import threading

def main():

    l = []

    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 7777))
    sock.listen(1)
    l.append(sock)

# Recepetion de la connexion
    while True:
        liste1, liste2, liste3 = select.select(l,[],[])
        for n in liste1:
            if n == sock:
                sockaccpt, addr = sock.accept()
                l.append(sockaccpt)
                print("Nouvelle connexion")
                print(addr)
            else:
                data = n.recv(1500)
                print(data.decode("utf-8"))
                n.send(data)
                if data == b'':
                    print(n.getsockname())
                    l.remove(n)
                    print("Fin de connexion")
                    n.close()



if __name__ == "__main__":
    main()
