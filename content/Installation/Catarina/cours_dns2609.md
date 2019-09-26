---
title: "DNS"
date: 2019-09-26T14:00:22+02:00
draft: false
---
# Le protocole DNS

Cours sur le DNS Domain Name System et le protocole correspondant.\
<u>Enseignant</u> : Catarina Christophe

> C'est quand même vachement pratique. Cependant à l'époque c'était pas comme ça et c'est pas rentré dans tous les moeurs.

## Noms d'hôtes
Avant tout passait par le fichier texte hosts.txt : `etc/hosts` qui contenait quelque information sur les noms de domaine.\
Aujourd'hui il y a le principe de l'annuaire qui est partagé entre tout le monde (les pages jaunes) qui est le DNS.

## Histoire
RFC 82 & RFC 83 qui sera vitale poru la création du DNS.\

## Rôle du DNS
Le DNS gêre aussi bien l'IPV6 que l'IPV4.

> Parallèle : Passé de l'IPV4 à l'IPV6 est une révolution.

Trouver un nom de domaine consiste à trouver l'adresse IP qui lui est associé. DNS utilise en général UDP et le port 53.\
Pour le cas d'un nom de domaine il y a à la fois une adresse IPV4 et IPV6.

## Hiérarchie du DNS
Exemple avec www.google.com :

+ Immédiatement sous la racine : TLD Top Level Domain.(com)
+ Ensuite en dessous il y a les domaines. (google.)
+ Puis l'hôte (www.)

## Résolution du nom par un hôte
Certains hôte comme le système local n'ont qu'une connaissance limité. Par conséquent l'interrogation des serveurs est renvoyé à un autre serveur etc.\
Une recherche s'effectue d'abord par le TLD. On va donc s'adresser au serveur qui connait par exemple de TLD "com".\
_Voir diapo_.

## Résolution inverse
Pour optimiser le routage on travail avec des adresses numérique.
*Voir diapo*

## Serveur DNS racine

## Principaux enregistrements DNS
