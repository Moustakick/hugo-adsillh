---
title: "Cours"
date: 2019-09-27T14:06:45+02:00
draft: false
---
## HTTP

> HTTP côté application

+ Séparation de fond et de forme
  + Fond : HTML
  + Forme : CSS

> Quand les journaliste contribue à un site web. Ils ont un formulaire depuis lequel ils créent leur site web. Puis le CSS et le code fait toute la mise en forme.

+ Différenciation statique et dynamique :

> La mise en place des pages dynamique a, de prime-abor, était faite pour les moteurs de recherche.

> Du statique avec PHP

> JS/FLASH/ActiveX : Assez rapidement inventé pour la création de jeux ou de rendu dynamique.

Notion d'applet et de servlet pour parler du bout de code qui s'exécute sur pour communiquer avec le serveur dans les pages dynamiques ou pour récupérer les données.

## Imbrication de protocole (VPN)

Carte réseau virtuel qui utilise un connexion via internet qui utilise une autre carte réseau plus loin sur l'internet.\
Sauf qu'il va passer par un autre point (une autre carte réseau) de préférence placé ailleurs sur le globe avant d'aller au point de destination.

{{<mermaid align="left">}}
graph LR;
    A(Demandeur) --> | Co securisée | B(VPN)
    B --> C(Connexion demandée)
{{< /mermaid >}}

Pour TOR le principe est le même mais il passe par 3 connexions différentes.

## ADSL

> Que ce passe t'il entre notre envoie de paquet IP et le FAI

Too long, did not write. En gros il y a 170M de ré-encapsulation.


# Chiffrement

+ Symétrique : Une clé, que l'on vient à s'échanger en privée. Cette même clé va servir à ouvrir et fermé.
+ Asymétrique : Une clé pour ouvrir et une clé pour fermé. Notion de clé publique et de clé privée.

Des gens peuvent utiliser la clé publique pour envoyer un message, et seul les possesseurs de la clé privée peuvent dechiffré le message.\
Quand la personne ayant un clé privée spécifique renvoie un message avec la clé privée, dechiffrable avec la clé publique. Advient la notion de signature ou d'authentification par clé privée. Non-répudiation.

La première fois que l'on se connecte en `ssh`. Il demande la vérification par le fingerprint afin valider la clé publique de la personne avec laquelle on communique.\
si la clé publique du destinataire change (détournement, reinstallation de la machine, etc.) alors `ssh` nous en informe.

Si nous ne voulons pas nous connecter avec mot de passe. Alors le client envoie la clé publique au serveur. Le serveur va alors lui demander de vérifier s'il s'agit bien de lui en lui envoyant des données à déchiffrer afin de vérifier.  

# Données structurées
