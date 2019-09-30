---
title: "Programmes et processus"
date: 2019-09-30T12:46:36+02:00
draft: false
---
Slide 03_Les-processus.pdf
# Programmes et Processus
Format ELF est le format executable que l’on va retrouver sur pas mal de programme UNIX.
```
file /lib/ls
```
Format adopté depuis plus de 20 ans.\
Regarder l’entête lu programme ls (avec la page wikipedia de ELF) : `head -c 64 /bin/ls | hexdump -C `. On y retrouve toutes les données indiqué par la commande `file /bin/ls`.

## Execution du main
(C) Argc : Le nombre de paramètres que l’on passe au programme.

## Exemples de programmes avec argv
On notera que sur chacun des programmes le premier argument de chaque programme est le nom du fichier qui est lancé. Dans des cas très spécfiique comme pour les liens symbolique, cela permet de modifié le comportement du programme en fonction de l’éxecutable du programme.

## Terminaison du programme
`echo $?` retourne le code de retour de la commande précédente.

## atexit
Permet de programmer une fonction qui se lance à la fermeture d’un programme.

## Anatomie d’un processus

> Voir schéma page 19.

## Création de processus
La fonction fork() duplique (clone) le processus appelant. Le processus dupliqué va devenir un processus « fils » du processus original dit « parent ». A partir du fork ils n’ont plus le même retour.

Si cela renvoie 0, le fork a fonctionné et on se trouve dans le processus fils. Autrement avec un retour > 0, le fork a échoué et on se trouve dans le processus parent.

*Devoir* : créer un programme qui prend tout ce qui est passé en argument. Pour ce qui est des programmes passés en argument, on l’execute et à la fin il indique si tout c’est bien passé sinon il retourne le code d’erreur. //le exec() du programme ce fait dans le fils
ex : `./prog ls – l /tmp`
