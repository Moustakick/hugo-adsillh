#!/usr/bin/python3
import os
import sys
import socket

def main():
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print ("Wrong arguments")
        sys.exit()

    print("Arguments OK")
    # Ameliorer la gestion d'erreur.

    link = sys.argv[1]

# traduction DNS de l'adresse et récuperation de deux tuples d'info IPv4 et IPv6 permettant la conception d'un objet socket
    ip = socket.getaddrinfo(sys.argv[1],"http",0,socket.SOCK_STREAM)

# unpack ipv6 tuple
    (family, type, proto, canonname, sockaddr) = ip[0]

# creation d'un objet socket avec les infos de l'adresse.
    sock = socket.socket(family,type,proto)

# connection a l'adresse
    sock.connect(sockaddr)

# envoie d'une requete avec une méthode spécifique
    sock.send(b"GET /\r\n\r\n")

# reception de la réponse avec une taille donnée
    print(sock.recv(128000))









if __name__ == "__main__":
    main()
