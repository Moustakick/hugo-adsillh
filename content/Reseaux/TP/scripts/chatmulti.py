#!/usr/bin/python3
import socket
import select
import threading

def encodeutf8(arg):
    return arg.encode("utf-8")

def f(s):
    while True:
        data = s.recv(1500)
        s.send(data)
        if data == 0:
            print("Fin de connexion")
            s.close()
            break


def main():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 7777))
    sock.listen(1)

# Recepetion de la connexion
    while True:
        (sockaccpt, addr) = sock.accept()
        print("Nouvelle connexion")
        print(addr)
        print(sockaccpt)
        threading.Thread(None, f, None, (sockaccpt,)).start()


# Gestion de la socket reçu
        # while True:
        #     data = sockaccpt.recv(1500)
        #     sockaccpt.send(data)
        #     if data == 0:
        #         print("Socket end")
        #         sockaccpt.close()
        #         break










if __name__ == "__main__":
    main()
