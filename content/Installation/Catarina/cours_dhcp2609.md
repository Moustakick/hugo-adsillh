---
title: "DHCP"
date: 2019-09-26T09:46:19+02:00
draft: false
---
Cours sur le protocole DHCP.\
<u>Enseignant</u> : Catarina Christophe

# Fonctionnement
Un DHCP serveur (deamon DHCP) écoute sur le réseau les gens qui demandent une adresse IP, pour les distribuer selon la configuration réseau.\
Une carte réseau ne sait pas comment se connecter au réseau. Par conséquent elle communique au réseau.

> A l'époque de Windows XP, la machine envoyait un broadcast sur l'internet pour obtenir un nom de domaine.

Normalement dans le domaine du broadcast il y a un serveur de DHCP actif. Et le serveur DHCP lui propose de prendre un adresse. Il attend ensuite confirmation de la part de la machine émetrice. Puis il valide et scelle l'offre.\
Le client va ensuite appeler sa propre adresse pour savoir si quelqu'un n'a pas répondu en même temps sur le réseau et n'ai pas la même adresse.

## Les baux
Les adresses sont défini avec un durée limitée, pour éviter que toutes les adresses soit attribuer même si l'appareil ne se connecte plus au réseau. **La durée d'attribution est défini dans le bail**.\
L'objectif par conséquent est de réflechir à une régle d'attribution des adresses en fonction des réseaux.

+ Par exemple dans un réseau où les ordinateurs vont se co et déco souvent alors on aura tendance à affecté des baux court.
+ Il y aussi des baux d'attribution fixe (MAC --> IP).

Normalement le serveur DHCP doit être dans la même branche réseau que les machines car le routeur ne fait pas la distibution du broadcast.

> Parallele : En informatique il y a des choses qui ont existés. Mais dans le hacking certaines choses vont être réutiliser. On reutilise pas mal de chose pour la construction de certaines commandes par exemple.

## Les requetes et les messages DHCP
+ DHCPDISCOVER : Pour localise les serveurs DHCP disponibles.
+ DHCPOFFER : Réponse du serveur à un message DHCPDISCOVER, qui contient les premiers paramètres.
+ DHCPREQUEST : Requête diverse du client par exemple pour prolonger son bail. (Aussi une réponse du client pour valider se bail).
+ DHCPDECLINE : Le client annonce au serveur que l'adresse est déjà utilisé.
+ DHCPACK : (ACK) Réponse du serveur qui contient des paramètres et l'adresse IP du client.
+ DHCPNAK : Réponse du serveur pour signaler au client que son bail est déchu ou si le client annonce une mauvaise configuration réseau.

> L'adresse MAC aujourd'hui n'est plus spécialement utilisée à cause du spoofing d'adresses pour l'attribution des adresses.\
La commande DHCPINFORM peut être lancé à la main depuis un client.

Séquence classique **DORA** : DHCP**D**ISCOVER --> DHCP**O**FFER --> DHCP**R**EQUEST --> DHCP**A**CK puis DHCPRELEASE (bien plus tard) :

{{<mermaid align="left">}}
graph LR;
    A[Client] -->|1. DHCPDISCOVER| B[Serveur]
    B -->|2. DHCPOFFER| A
    A -->|3. DHCPREQUEST| B
    B -->|4. DHCPACK| A
{{< /mermaid >}}
___
### Trames
Voir le diapo : trames/options/etc
___
### Wireshark
Voir le diapo.
___
### Bibliographie

> man in the middle proxy
