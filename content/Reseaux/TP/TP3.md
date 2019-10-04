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
