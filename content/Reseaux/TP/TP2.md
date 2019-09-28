---
title: "TP2 Reseaux"
date: 2019-09-27T15:24:05+02:00
draft: false
---
TP : http://dept-info.labri.fr/~thibault/Reseau/TP2.pdf

Correction : http://dept-info.labri.fr/~thibault/Reseau/TP2-corr.pdf

> Des commandes : \
 echo 1 > /proc/sys/net/ipv4/ip_forwar \
 tcpdump


# Netcat
-Avec la commande `nc machineduvoisin 12345`. On peut observer ensuite dans netstat `netstat
-Ainet -Ainet6` les nouvelles connexions établies.

-Transmission des messages "woof" & "la" confirmed.

-Il faut rediriger la sortie de la commande nc (avec `>`) vers un fichier puis du côté de l'envoyeur envoyer le contenu du fichier danc nc (`< test.txt nc ---` ).

# 2 Services au CREMI : LDAP & NFS
-Il y a plusieurs serveur pour la redondance des serveurs dans le cadre où un serait down.\
Le port de ce service est le : 389.

-Sur cette commande nous pouvons voir que le disque est monté sur /autofs/unityaccount/cremi.\
Nous pouvons aussi y voir le nom du serveur qui est : unityaccount.

# 3 Connexion à une machine distante avec SSH
C'est grâce au fait que tout est calculé sur la machine sur laquelle on fait le ssh puis envoyé au client et affiché.
