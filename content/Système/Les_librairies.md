---
title: "Les librairies"
date: 2019-11-12T12:46:36+02:00
draft: false
---
Slide 09-Librairies.pdf
# Les librairies
Nous connaissons déjà les chemins normés pour les exécutables comme $PATH.\
Maintenant il existe des chemins normés pour les librairies : "/lib[64,32,...]/ld-l..." mais pour avoir une vria vision de l'intégralité des librairies nous pouvons aller dans "/usr/lib/" ou "/usr/lib/x86_64-linux-gnu/".

Historiquement toutes les librairies étaient dans "/usr/lib".

Prenant l'exemple de la librairie libpng : si on fait un `file libpgn*` dans "/usr/lib/x86_64-linux-gnu"  on obtient :
```bash
mocafrain@page:/usr/lib/x86_64-linux-gnu-14:52:02$ file libpng*
libpng12.so.0:       symbolic link to /lib/x86_64-linux-gnu/libpng12.so.0
libpng16.a:          current ar archive
libpng16.so:         symbolic link to libpng16.so.16.28.0
libpng16.so.16:      symbolic link to libpng16.so.16.28.0
libpng16.so.16.28.0: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=c08e2e9d66bfee4e5a9c364bd955ded106eea226, stripped
libpng.a:            symbolic link to libpng16.a
libpnglite.so:       symbolic link to libpnglite.so.0
libpnglite.so.0:     ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=ed96d693edbfe66020aab003fe5de3625b51d0c5, stripped
libpng.so:           symbolic link to libpng16.so
```
Le seule fichier spécifique (hors lien symbolique) est le fichier "ELF". La chose importante à remarqué est le détail du fichier qui indique l'architecture de l'ordinateur, comme pour le répertoire.

L'idée d'avoir architecturé les librairies ainsi, c'est pour qu'il y ai une co-installation de plusieurs architectures. Une autre idée c'est pour que l'on puisse faire de la cross-compilation.

## Création d'un programme
Création d'un programme basique "hello_world.c"

Après compilation du programme, nous avons obtenu un fichier exécutable. Maintenant si on fait un `file ./hello_world` on obtient les informations suivantes :
```bash
mocafrain@page:/autofs/unitytravail/travail/mocafrain/Cours/hugo-adsillh/content/Système/Scripts-15:17:42$ file ./hello_world
./hello_world: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=d4d582409c72b0c9b202265c467f24bf860e3ad7, not stripped
```

On obtient toutes informations comme l'architecture etc.

Si on retire le droit d'execution du fichier "hello_world", nous allons obtenir une erreur du style "permission non accordée".
Cependant si on l'execute en passant par l'interpréteur du programme directement avec une commande du genre : `/lib64/ld-linux-x86-64.so.2 ./hello_world` alors le code est bien interprété par la librairie et fonctionnel.

## Les fichiers objets

## Edition de liens dynamique avec une librairie tierce

Commande `ldd` qui permet d'obtenir les bibliothèques (partagées) nécessaires au programme.

 
