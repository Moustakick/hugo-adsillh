#!/usr/bin/python3
import socket
import select
import threading

def main():


    l = []

    nick = {}


    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 7777))
    sock.listen(1)
    l.append(sock)
    nick[sock] = "Serveur"


    while True:
        liste1, liste2, liste3 = select.select(l,[],[])
        for n in liste1:
# Nouveau client
            if n == sock:
                sockaccpt, addr = sock.accept()

                l.append(sockaccpt)
                nick[sockaccpt] = ""
                for i in l:
                    if i == sock:
                        print("Nouvelle connexion\n")
                    elif i == n:
                        pass
                    else:
                        i.send(b"Nouvelle connexion\n")
                print(addr)
# Reception et envoie
            else:
                data = n.recv(1500)
                msg = data.decode("utf-8")

# Commande NICK
                if msg.startswith("NICK"):
                    print("Nick command used")

                    oldnick = nick[n].encode("utf-8")
                    nick[n]= msg[5:]
                    for i in l:
                        if i == sock or i == n:
                            pass
                        else:
                            nicktmp = nick[n].encode("utf-8")
                            i.send(b"User "+oldnick+b" set his nickname to "+nicktmp+b"\n")

# Warning NICKNAME
                if nick[n] == "":
                    n.send(b"SET A NICKNAME\n")

# Commande MSG
                elif msg.startswith("MSG"):
                    for i in l:
                        if i == sock or i == n:
                            pass
                        else:
                            nicktmp = nick[n].encode("utf-8")
                            i.send(nicktmp+b" :"+data[3:])

# Commande LIST
                elif msg.startswith("LIST"):
                    for i in l:
                        if i == sock:
                            pass
                        else:
                            nicktmp = nick[i].encode("utf-8")
                            n.send(nicktmp)

# Commande KILL
                elif msg.startswith("KILL"):
                    nicktokill = msg[5:]
                    for i in l:
                        if nick[i] == nicktokill:
                            for j in l:
                                if j == sock:
                                    print("USER KILLED")
                                else:
                                    j.send(b"A user has been killed\n")

                            nick[i] = ""
                            i.close()
                            l.remove(i)









                if data == b'':
                    print(n.getsockname())
                    l.remove(n)
                    print("Fin de connexion")
                    n.close()



if __name__ == "__main__":
    main()
