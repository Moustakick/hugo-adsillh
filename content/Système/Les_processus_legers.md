---
title: "Les processus légers"
date: 2019-10-01T14:16:36+02:00
draft: false
---
https://openics.org/teaching/adsillh/05_Les-processus-legers.pdf

# Les processus légers (Thread)
 Les ***processus légers*** ou ***threads*** en anglais sont aussi appelés ***"fil d'execution"***.

## Processus et processus légers
Les processus légers sont de mini processus qui fonctionnent dans un processus normal.

IPC = Inter Process Communication.\
Les signaux sont un mécanisme d'IPC.\
--> C'est ce qui va permettre la communication entre les processus.

Dans les processus legers la communication via IPC n'ont pas grand interet car les processus leger partage le même emplacement mémoire, par conséquent partage les mêmes variables etc.

## Anatomie d'un processus en mémoire
Ce que l'on voit dans la figure en page 5, c'est que dans l'espace mémoire, au lieux d'avoir une seule pile d'execution, le processus leger va creer une autre pile d'execution (stack) dans le même emplacement mémoire.

> Il va y avoir plusieurs stack différents dans le emplacement mémoire du processus. **page 6**

> Dans le programme `htop` nous pouvons voir les processus légers d'une couleur différente (vert) des processus classique (blanc).

## Informations partagées par les processus légers
*Voir liste sur le diapo*

> Dans Chrome au début ils utilisaient beaucoup les processus legers, mais ils ont switché pour des processus normaux pour des raisons de sécurité. Parce que si chaque onglet uttilise un processus légers, alors ils utilisent le même emplacement mémoire etc.. et ça peut poser des problèmes de sécurité.

## POSIX Thread API
Pour en revenir à UNIX, l'API Pthread se place dans un concept de normes : SUSv3 et est issue de POSIX.1c.

## Convention de l'API
Au lieu de retourner 0 pour un succès et -1 pour un échec. Un thread va retourner 0 pour le succès mais si il retourne autre chose alors il s'agit d'une erreur.

## Création d'un processus léger
Le processus quand il démarre si il supporte les processus légers même si il n'en lance pas, il va se comporter comme un processus légers que l'on appel processus léger principal.

## Terminaison d'un processus léger
Le vocabulaire veut que l'on dise que l'on "annule" un processus léger quand on le termine de l'exterieur.

## Attente de la fin d’un autre processus léger
Pthread_join permet d'attendre la fin d'un processus léger.

A la différence de la fonction wait_pid() pour les processus, pour les threads il n'y pas moyen d'attendre la fin le thread de son choix.

## Hello World && Hello World - multithread
Programme d'exemple pour la création de threads en C.\
Une différence à noté est que pour la compilation du programme nous devons passé en argument "-pthread" en plus pour que tout ce passe correctement.

test mermaid :

pie
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15 
