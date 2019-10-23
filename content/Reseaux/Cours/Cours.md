---
title: "Cours"
date: 2019-09-27T14:06:45+02:00
draft: false
---
## HTTP

> HTTP c�t� application

+ S�paration de fond et de forme
  + Fond : HTML
  + Forme : CSS

> Quand les journaliste contribue � un site web. Ils ont un formulaire depuis lequel ils cr�ent leur site web. Puis le CSS et le code fait toute la mise en forme.

+ Diff�renciation statique et dynamique :

> La mise en place des pages dynamique a, de prime-abor, �tait faite pour les moteurs de recherche.

> Du statique avec PHP

> JS/FLASH/ActiveX : Assez rapidement invent� pour la cr�ation de jeux ou de rendu dynamique.

Notion d'applet et de servlet pour parler du bout de code qui s'ex�cute sur pour communiquer avec le serveur dans les pages dynamiques ou pour r�cup�rer les donn�es.

## Imbrication de protocole (VPN)

Carte r�seau virtuel qui utilise un connexion via internet qui utilise une autre carte r�seau plus loin sur l'internet.\
Sauf qu'il va passer par un autre point (une autre carte r�seau) de pr�f�rence plac� ailleurs sur le globe avant d'aller au point de destination.

{{<mermaid align="left">}}
graph LR;
    A(Demandeur) --> | Co securis�e | B(VPN)
    B --> C(Connexion demand�e)
{{< /mermaid >}}

Pour TOR le principe est le m�me mais il passe par 3 connexions diff�rentes.

## ADSL

> Que ce passe t'il entre notre envoie de paquet IP et le FAI

Too long, did not write. En gros il y a 170M de r�-encapsulation.


# Chiffrement

+ Sym�trique : Une cl�, que l'on vient � s'�changer en priv�e. Cette m�me cl� va servir � ouvrir et ferm�.
+ Asym�trique : Une cl� pour ouvrir et une cl� pour ferm�. Notion de cl� publique et de cl� priv�e.

Des gens peuvent utiliser la cl� publique pour envoyer un message, et seul les possesseurs de la cl� priv�e peuvent dechiffr� le message.\
Quand la personne ayant un cl� priv�e sp�cifique renvoie un message avec la cl� priv�e, dechiffrable avec la cl� publique. Advient la notion de signature ou d'authentification par cl� priv�e. Non-r�pudiation.

La premi�re fois que l'on se connecte en `ssh`. Il demande la v�rification par le fingerprint afin valider la cl� publique de la personne avec laquelle on communique.\
si la cl� publique du destinataire change (d�tournement, reinstallation de la machine, etc.) alors `ssh` nous en informe.

Si nous ne voulons pas nous connecter avec mot de passe. Alors le client envoie la cl� publique au serveur. Le serveur va alors lui demander de v�rifier s'il s'agit bien de lui en lui envoyant des donn�es � d�chiffrer afin de v�rifier.  

# Donn�es structur�es
