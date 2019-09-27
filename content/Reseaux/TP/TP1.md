---
title: "TP1 Reseaux"
date: 2019-09-27T14:06:45+02:00
draft: false
---
TP : http://dept-info.labri.fr/~thibault/Reseau/TP1.pdf

Correction : http://dept-info.labri.fr/~thibault/Reseau/TP1-corr.pdf

# Interfaces réseau et Adresse IP
-Adresses :

+ eth0 :
  + IPv4 :
    + 10.0.7.19 /24
    + MTU : 9000
  + IPv6 :
    + global : 2001:660:6101:800:7::19 /80
    + link : fe80::da9e:f3ff:fe10:2dc1 /64
    + MTU : 9000
+ lo (localhost) :
  + IPv4 :
    + 127.0.0.1 /8
    + MTU : 65536
  + IPv6 :
    + ::1 /128
    + MTU : 65536

-L'interface "lo" correspond au localhost.

-Le MTU n'est pas le même et est plus elevé pour localhost car pour l'envoie de paquet locaux il n'y a pas de contrainte matériel.

-Ok. Ping en IPv6 et IPv4 du voisin validé.

# Protocole ARP
-Ok. `/usr/sbin/arp -n`

-Ok. Apparition de la machine pingé dans la table ARP.

-Ok. `ip neigh ls`

# Résolution de noms (DNS)
-`cat /etc/resolv.conf`. Il y a plusieurs adresses IP pour plusieurs serveur DNS pour faire de la tolérance de panne : Résiliance des serveurs et Répartition des charges.

-Avec http://www/ : Redirection vers le site du cremi www.emmi.u-bordeaux.fr.

-`nslookup yahoo.com` : plusieurs adresse IPv4 pour les mêmes raisons de tolérance de panne et aussi pour la grande quantité d'utilisateurs.\
Pour l'IPv6 : `nslookup -query=AAAA yahoo.com` --> Il y a aussi plusieurs adresses en IPv6.\


# Configuration d'un réseau local
-`ifconfig -a` : display toutes les interfaces même inactives.\
Deux interfaces : lo (localhost) qui est active et eth0 qui est inactive.

-Setup interface *eth0* :

+ Adresse du réseau : 192.168.0.0
+ Masque du réseau : 255.255.255.0 /24
+ Plage adresse IP : 192.168.0.[1-254]. (.0, .255 étant louées)

-Commandes pour la configuration des interfaces :
```
ifconfig eth0 up
ifconfig eth0 192.168.0.1 netmask 255.255.255.0 up
```
-`ping 192.168.0.1` --> `tcpdump -i eth0` : Récuperation de du ping valide.

-Non toutes les machines recoivent le `ping -b` mais aucune n'y répond.\
Avec la commande `echo 0 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts` les machines répondent au ping en broadcast.

-Configuration du fichier `/etc/network/interfaces` :
```
allow-hotplug eth0
iface eth0 inet static
  address 192.168.0.1
  broadcast 192.168.0.255
  netmask 255.255.255.0
```
