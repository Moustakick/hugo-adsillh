---
title: "TP3 Analyse et génération"
date: 2019-10-04T14:06:45+02:00
draft: false
---
http://dept-info.labri.fr/~thibault/Reseau/TP3.pdf

# Analyse : wireshark
Les secondes à côté des questions correspond à l'heure à laquelle la trame correspondante a été capturé.

## Un premier ping
DNS : 193.50.11.150\
Port : 53\
Domaine à résoudre : www.google.com\
Le résultat :
```
4	2.282683	193.50.111.150	193.50.110.76	DNS	313	Standard query response 0x0d6b A www.google.fr CNAME www.google.com CNAME www.l.google.com A 209.85.229.103 A 209.85.229.104 A 209.85.229.105 A 209.85.229.106 A 209.85.229.147 A 209.85.229.99 NS f.l.google.com NS g.l.google.com NS a.l.google.com NS b.l.google.com NS d.l.google.com NS e.l.google.com
```

L'adresse MAC est la même car notre machine de test, par ethernet, chercher d'abord à faire passer sa trame par sa passerelle. Les deux messages DNS et ICMP passent par la même passerelle.\
L'adresse IP est différente du fait que la machine de destination "finale" (209.85.229.103) à une IP connue différente de l'IP du DNS local (193.50.11.150).

Latence : 2.314204 - 2.283083 = 0.031121s

## Un deuxieme ping
Ce deuxieme ping est effectué vers une machine du même réseau que nnotre machine de test, par conséquent : Il n'y a pas de sorti du réseau, donc pas de passage vers un passerelle, et pas besoin d'effectuer une résolution DNS étant donné qu'on ping une adresse IPv4 directement. Le temps de latence en est donc considérablement réduit ( 0.00017s).

## Une page web
Les couleurs correspondent à un type d'échange.\
URL complète demandée : [Full request URI: http://dept-info.labri.fr/~thibault/]

Les autres requêtes HTTP correspondent au requêtes de ressources sur une page web, comme les photos ou autres.

## Une deuxieme page web
L'utilisateur a ouvert un lien vers une autre page.

## CUPS (Common UNIX Printing System)
Nom : DESKJET_895C

## Lire des mails
Pass : foobar

# Génération : scapy
Scapy : logiciel libre de manipulation de paquets réseau écrit en python.

Daytime : http://dept-info.labri.fr/~thibault/Reseau/daytime.py

Resultat :
```
15:19:10.723564 ARP, Request who-has 147.210.0.1 tell 147.210.0.2, length 46
15:19:10.723579 ARP, Reply 147.210.0.1 is-at aa:aa:aa:aa:00:00 (oui Unknown), length 28
15:19:10.724470 IP 147.210.0.2.12345 > 192.168.0.2.daytime: UDP, length 7
15:19:10.725568 IP 192.168.0.2.daytime > 147.210.0.2.12345: UDP, length 26
15:19:10.725767 ARP, Request who-has 147.210.0.1 tell 147.210.0.2, length 46
15:19:10.725771 ARP, Reply 147.210.0.1 is-at aa:aa:aa:aa:00:00 (oui Unknown), length 28
15:19:10.726054 IP 147.210.0.2 > 192.168.0.2: ICMP 147.210.0.2 udp port 12345 unreachable, length 62
```

# Firewall

> Au sein d’un réseau d’entreprise, quel différence y-a-t’il entre la DMZ et le réseau
interne des employés ?

Contrairement au réseau interne des employés la DMZ est un zone peu ou pas protégée. De plus elle n'est pas reliée directement au réseau interne, pour eviter les attaques depuis internet.


> Autoriser le ping (c’est-à-dire le protocole icmp) du réseau Interne vers Internet, sans
autoriser l’inverse.

```
iptables -A FORWARD -i eth2 -o eth0 -p icmp -j ACCEPT
```

Message d'envoie côté "Interne" :

```bash
root@nile:~# ping 147.210.0.2
PING 147.210.0.2 (147.210.0.2) 56(84) bytes of data.
```

TCPDUMP côté "Internet" :

```bash
root@opeth:~# tcpdump
[  929.012581] Bluetooth: Core ver 2.21
[  929.013604] NET: Registered protocol family 31
[  929.014893] Bluetooth: HCI device and connection manager initialized
[  929.018429] Bluetooth: HCI socket layer initialized
[  929.020046] Bluetooth: L2CAP socket layer initialized
[  929.021604] Bluetooth: SCO socket layer initialized
[  929.037498] Netfilter messages via NETLINK v0.30.
[  929.060734] device eth0 entered promiscuous mode
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
14:23:48.410684 ARP, Request who-has 147.210.0.2 tell 147.210.0.1, length 46
14:23:48.410708 ARP, Reply 147.210.0.2 is-at aa:aa:aa:aa:01:00 (oui Unknown), length 28
14:23:48.410960 IP 192.168.1.2 > 147.210.0.2: ICMP echo request, id 1235, seq 1, length 64
14:23:48.410976 IP 147.210.0.2 > 192.168.1.2: ICMP echo reply, id 1235, seq 1, length 64
14:23:49.418561 IP 192.168.1.2 > 147.210.0.2: ICMP echo request, id 1235, seq 2, length 64
```

Le message icmp va bien vers "internet" mais il n'y a aucun retour côté "interne".

Avec la commande :

```
iptables -A FORWARD -m state - -state RELATED,ESTABLISHED -j ACCEPT
```

Ping côté "interne" vers "internet" :

```bash
root@nile:~# ping 147.210.0.2
PING 147.210.0.2 (147.210.0.2) 56(84) bytes of data.
64 bytes from 147.210.0.2: icmp_seq=1 ttl=63 time=0.639 ms
64 bytes from 147.210.0.2: icmp_seq=2 ttl=63 time=0.694 ms
64 bytes from 147.210.0.2: icmp_seq=3 ttl=63 time=0.718 ms
64 bytes from 147.210.0.2: icmp_seq=4 ttl=63 time=0.679 ms
```

Il y a désormais une réponse au message icmp 'ping' envoyé.

> Autorisez l’accès au web depuis les machines du réseau interne. Faire un test avec
wget

Commande :
```bash
iptables -A FORWARD -i eth2 -o eth0 -p tcp --dport 80 -j ACCEPT
```

`wget` côté interne :

```bash
root@nile:~# wget 147.210.0.2
--2019-10-11 14:36:22--  http://147.210.0.2/
Connecting to 147.210.0.2:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10701 (10K) [text/html]
Saving to: ‘index.html.1’

index.html.1        100%[===================>]  10.45K  --.-KB/s    in 0s      

2019-10-11 14:36:22 (266 MB/s) - ‘index.html.1’ saved [10701/10701]
```

`tcpdump` côté "internet" :

```bash
root@opeth:~# tcpdump
[ 1856.453451] device eth0 entered promiscuous mode
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
14:38:49.287285 IP 192.168.1.2.55258 > 147.210.0.2.http: Flags [S], seq 1744401285, win 29200, options [mss 1460,sackOK,TS val 389605 ecr 0,nop,wscale 6], length 0
14:38:49.287316 IP 147.210.0.2.http > 192.168.1.2.55258: Flags [S.], seq 3232724567, ack 1744401286, win 28960, options [mss 1460,sackOK,TS val 389595 ecr 389605,nop,wscale 6], length 0
14:38:49.287859 IP 192.168.1.2.55258 > 147.210.0.2.http: Flags [.], ack 1, win 457, options [nop,nop,TS val 389605 ecr 389595], length 0
14:38:49.291338 IP 192.168.1.2.55258 > 147.210.0.2.http: Flags [P.], seq 1:139, ack 1, win 457, options [nop,nop,TS val 389606 ecr 389595], length 138: HTTP: GET / HTTP/1.1
14:38:49.291375 IP 147.210.0.2.http > 192.168.1.2.55258: Flags [.], ack 139, win 470, options [nop,nop,TS val 389597 ecr 389606], length 0
14:38:49.291961 IP 147.210.0.2.http > 192.168.1.2.55258: Flags [.], seq 1:5793, ack 139, win 470, options [nop,nop,TS val 389597 ecr 389606], length 5792: HTTP: HTTP/1.1 200 OK
14:38:49.292121 IP 147.210.0.2.http > 192.168.1.2.55258: Flags [P.], seq 5793:11013, ack 139, win 470, options [nop,nop,TS val 389597 ecr 389606], length 5220: HTTP
14:38:49.292623 IP 192.168.1.2.55258 > 147.210.0.2.http: Flags [.], ack 11013, win 801, options [nop,nop,TS val 389607 ecr 389597], length 0
14:38:49.297182 IP 192.168.1.2.55258 > 147.210.0.2.http: Flags [F.], seq 139, ack 11013, win 801, options [nop,nop,TS val 389608 ecr 389597], length 0
14:38:49.297226 IP 147.210.0.2.http > 192.168.1.2.55258: Flags [F.], seq 11013, ack 140, win 470, options [nop,nop,TS val 389598 ecr 389608], length 0
14:38:49.298419 IP 192.168.1.2.55258 > 147.210.0.2.http: Flags [.], ack 11014, win 801, options [nop,nop,TS val 389608 ecr 389598], length 0
```

Il y a bien une communication et un retour par le port 80 "http/web" entre les deux réseaux.

> Autorisez grave à accèder au serveur ssh (port 22) de dt. Faire un test avec le compte toto (mot de passe toto).

Commande :
```bash
iptables -A FORWARD -i eth3 -o eth1 -p tcp --dport 22 -j ACCEPT
```

`ssh toto@192.168.0.3` côté 'grave' :

```bash
root@grave:~# ssh toto@192.168.0.3
The authenticity of host '192.168.0.3 (192.168.0.3)' can't be established.
ECDSA key fingerprint is SHA256:b2tuLYwJkZtgLmH5GkvZyi2JWc/v8plfeyPmuz9cxmU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.0.3' (ECDSA) to the list of known hosts.
toto@192.168.0.3's password:
Linux dt 4.7.0-1-amd64 #1 SMP Debian 4.7.2-1 (2016-08-28) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
toto@dt:~$
```

`tcpdump` côté 'dt' :

```bash
root@dt:~# tcpdump
[ 2441.101670] device eth0 entered promiscuous mode
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
14:48:35.877652 IP 172.16.0.2.55872 > 192.168.0.3.ssh: Flags [S], seq 2546268247, win 29200, options [mss 1460,sackOK,TS val 536244 ecr 0,nop,wscale 6], length 0
14:48:35.877670 IP 192.168.0.3.ssh > 172.16.0.2.55872: Flags [S.], seq 399177825, ack 2546268248, win 28960, options [mss 1460,sackOK,TS val 536255 ecr 536244,nop,wscale 6], length 0
14:48:35.877945 IP 172.16.0.2.55872 > 192.168.0.3.ssh: Flags [.], ack 1, win 457, options [nop,nop,TS val 536245 ecr 536255], length 0
14:48:35.878070 IP 172.16.0.2.55872 > 192.168.0.3.ssh: Flags [P.], seq 1:33, ack 1, win 457, options [nop,nop,TS val 536245 ecr 536255], length 32
14:48:35.878075 IP 192.168.0.3.ssh > 172.16.0.2.55872: Flags [.], ack 33, win 453, options [nop,nop,TS val 536255 ecr 536245], length 0
14:48:35.883869 IP 192.168.0.3.ssh > 172.16.0.2.55872: Flags [P.], seq 1:33, ack 33, win 453, options [nop,nop,TS val 536256 ecr 536245], length 32
14:48:35.885304 IP 172.16.0.2.55872 > 192.168.0.3.ssh: Flags [.], ack 33, win 457, options [nop,nop,TS val 536246 ecr 536256], length 0
[...]
```

> Autorisez l’accès depuis n’importe où vers le serveur web de syl (port 80). Faites un
test avec wget.

Commande :

```bash
iptables -A FORWARD -i * -d 192.168.0.2 -p tcp --dport 80 -j ACCEPT
```

Connexion avec `wget`, message et `tcpdump` fonctionnels.

> Depuis opeth et grave, testez votre firewall sur la DMZ avec nmap !

```bash
root@grave:~# nmap 147.210.0.2

Starting Nmap 7.12 ( https://nmap.org ) at 2019-10-11 14:51 UTC
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.18 seconds
root@grave:~# nmap 147.210.0.2

Starting Nmap 7.12 ( https://nmap.org ) at 2019-10-11 14:57 UTC
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.03 seconds

```

```bash
root@opeth:~# nmap 147.210.0.2

Starting Nmap 7.12 ( https://nmap.org ) at 2019-10-11 14:58 UTC
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 147.210.0.2
Host is up (0.0000050s latency).
Not shown: 996 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
23/tcp open  telnet
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.59 seconds
root@opeth:~#
```

> Pas sûr que ce soit très fonctionnel.

# Bonus : Et le réseau sous windows ?

```

```
