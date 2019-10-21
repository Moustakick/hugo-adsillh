#!/usr/bin/python3
import socket
import select
import threading


def main():

    l = []

    nick = {}

    channel = {}
    channelUser = {}


    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 7777))
    sock.listen(1)
    l.append(sock)
    nick[sock] = "Serveur"


###########################################################################

    def sendall(message):
        for i in l:
            if i == sock:
                print(message)
            elif i == n:
                pass
            else:
                i.send(message.encode("UTF-8")+b"\n")



##########################################################################

    def command(com, msg, sck):

        msgbytes = msg.encode("UTF-8")
        # Commande NICK
        if com == "SEND":
            if msg[:-1] == "HELP":
                sck.send(b"Commande list : MSG, NICK, JOIN, LIST [CUSERS, USERS], KICK, KILL.\n")
            if msg[:-1] == "NUDES":
                sck.send(b"Oh you eheh\n")


        if com == "NICK":
            print("USER INFO : Nick command used")
            oldnick = nick[n].encode("utf-8")
            oldnickstr = nick[n]
            nick[n]= msg[:-1]
            nicktmp = nick[n].encode("utf-8")

            for i in l:
                if i == sock:
                    print("INFO : User "+oldnickstr+" set his nickname to "+nick[n])
                elif i == n:
                    i.send(b"-- Nickname set to "+nicktmp+b"\n")
                else:
                    i.send(b"INFO : User "+oldnick+b" set his nickname to "+nicktmp+b"\n")

        if com == "JOIN":
            sck.send(b"Joining channel "+msgbytes)
            channelUser[sck]=int(msg)
            return 0
        # Warning NICKNAME
        elif nick[n] == "":
            n.send(b"-- SET A NICKNAME with the commande NICK\n")
            return 0

        if channelUser[sck]==0:
            sck.send(b"Please JOIN [1-100] a channel before talking\n")
            return 0

        # Commande MSG
        elif com == "MSG":
            for i in l:
                if i == sock:
                    pass
                elif i == sck:
                    i.send(b"Message -> Me : "+msgbytes)
                # elif
                #         # i.send(b"Message -> "+nicktmp+b" :")
                #         i.send(b"Message -> :")
                else:
                    if channelUser[i] == channelUser[sck]:
                        nicktmp = nick[sck].encode("utf-8")
                        i.send(b"Message -> "+nicktmp+b" : "+msgbytes)
                    pass

        # Commande LIST
        elif com == "LIST":
            if msg[:-1] == "USERS":
                for i in l:
                    if i == sock:
                        pass
                    else:
                        nicktmp = nick[i].encode("utf-8")
                        sck.send(nicktmp+b"\n")
            if msg[:-1] == "CUSERS":
                for i in l:
                    if i == sock:
                        pass
                    else:
                        if channelUser[i] == channelUser[sck]:
                            nicktmp = nick[i].encode("utf-8")
                            sck.send(nicktmp+b"\n")
            if msg[:-1] != "CUSERS" and msg[:-1] != "USERS":
                sck.send("LIST CUSERS for all the users\nor LIST USERS for the users of your current channel. ")

        # Commande KILL
        elif com == "KILL":
            nicktokill = msg[:-1]
            for i in l:
                if nick[i] == nicktokill:
                    sendall("INFO : A user has been killed")
                    nick[i] = ""
                    i.close()
                    l.remove(i)

        elif com == "KICK":
            nicktokill = msg[:-1]
            for i in l:
                if nick[i] == nicktokill:
                    sendall("INFO : A user has been kick Lee-sin style")
                    channelUser[i]=0

        elif com == "PART":
            sck.send(b"Leaving the channel and returning to the hobby.\n")
            channelUser[sck]=0
            print("User "+nick[sck]+" returned to the hobby")





##########################################################################


# Select serveur permettant de gerer les clients
    while True:
        liste1, liste2, liste3 = select.select(l,[],[])
        for n in liste1:
# Nouveau client
            if n == sock:
                sockaccpt, addr = sock.accept()

                l.append(sockaccpt)
                nick[sockaccpt] = ""
                channelUser[sockaccpt]=0
                sendall("INFO : NEW CONNECT")
                sockaccpt.send(b"Please set a nickname with NICK and join a channel with JOIN [ChannelNumber]\nYou can always cry for help with the command SEND HELP.\n")

                print(addr)
# Reception et envoie
            else:
                data = n.recv(1500)
                msg = data.decode("utf-8")
                com = ""

                if data == b'':
                    print(n.getsockname())
                    l.remove(n)
                    print("INFO : CONNECT ENDED")
                    n.close()

                if " " in msg:
                    com = msg[:msg.index(" ")]
                    msg = msg[msg.index(" ")+1:]
                    # print(com)
                    # print(msg)
                    # print(n)
                    command(com, msg, n)
                else:
                    com = msg[:-1]
                    command(com, "", n)






if __name__ == "__main__":
    main()
