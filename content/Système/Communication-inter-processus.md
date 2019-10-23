---
layout: "post"
title: "Communication_inter-processus"
date: "2019-10-22 14:11"
---
https://openics.org/teaching/adsillh/07_Communication-Inter-Processus.pdf

# Communication inter-processus - IPC
Pour l'instant nous avons vu 2 mécanismes de communication inter-processus différents :

+ Les signaux
+ Les tubes

3 mécanisme de communication entre processus que l'on nomme IPC (Inter Processus Communication) :

1. Les files de messages (message queues)
2. La mémoire partagée (share memory)
3. Les sémaphores (semaphores)

## API de IPC
1. System V IPC : Api qui n'est pas fondé sur la philosophie UNIX.
2. IPC Posix : Que nous allons utiliser. Plus moderne.

## Files de messages
Les IPC sont des files de messages. Comme pour les tubes sauf que nous travaillons pas sur des flux d'octets mais sur des messages de longueur variable.

## Ouvrir une file de messages

mqd_t mq_open(const char \*name, int flags);

name :  nom de la file (doit commencer par un / et ne pas en
comporter d’autres)\
flags, mode:  arguments identiques `a ceux de open\
attr :  attributs de la file (nombre maximal de messages, taille maximal d’un message)


## Mémoire partagée

Nous allons creer une zone de mémoire partagée. Ensuite nous allons la projeter dans l'espace mémoire du procesus (en tant que variable).

La variable est stockée dans un fichier dans /etc/shm/ et est stockée sur 8octets.

## Sémaphores

Permet d'organiser l'accès concurrent à des ressources partagées.
