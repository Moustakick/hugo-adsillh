---
title: "Les signaux"
date: 2019-09-30T13:33:38+02:00
draft: false
---
https://openics.org/teaching/adsillh/04_les-signaux.pdf
# Les signaux

Les signaux = interruptions logiciels

**Asynchrone** → on ne peut pas vriament predire quand le recepteut du signal va recevoir l’information.

Plusieurs catégories de signaux :

+ Signaux utilisateurs (ctrl+x, ctrl+z)
+ Fautes matérielles (division par zéro)
+ Fautes logicielles (erreur d’ »criture dans un tube)
+ Envoie d eplusieurs signaux direct entre processus (man 2 kill)
+ Envoie de signaux par l’utilisateur (man 1 kill)

## Traitement des signaux

Core : Arrive des fois quand un programme plante (créer des fichiers core). Il s’agit de l’image du processus au moment où il a planté.

Cont : la commande fg consiste par exemple à reprendre ce processus grâce à ce signal.

## Liste des Signaux
Les signaux notables :

+ SIGINT
+ SIGTERM
+ SIGPIPE : Par défaut terminera le programme. (Des fois pas gerer, message : « broken pipe »)
+ SIGSTOP

> Voir slides pour plus de details.
