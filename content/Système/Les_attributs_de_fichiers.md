---
title: "Les attributs de fichiers"
date: 2019-11-05T12:06:02+02:00
draft: false
---
# Les attributs de fichiers
Les attributs de fichiers comme les meta-données sont toutes les informations relatif à la vie du fichier.\
pe : taille du fichier, permissions d'accès, propriétaire et groupe, horodatages, etc..

## Système de fichiers
Un périphérique de stockage est une disque physique est une unité de stockage vierge. Avec ça on ne fait pas grand chose. \
(Avant avec grub et tout ça) Maintenant on a une système qui s'appel (U)EFI qui permet de définir une interface logiciel entre le firmware et le OS. Il sert aussi à partitionner les disques.

Avec la commande `lsblk` on peut se rendre compte du partitionnement du système.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Un système de fichier se creer grâce à un outil. Sur Unix il s'agit de ext4.

FAT : Liste chainée de bloc.

Page 4 - représentation des partitions :\
Notion de super block (et ses copies). C'est dans ce super block qu'on va pouvoir obtenir le nom des fichiers liés à une i-nodes. Basiquement ils sont liés à des adresses pour trouver ces dossiers. Un dossier référence une certaint nombre d'i-nodes.

### Creation d'un système de fichier dans une fichier

Allocation de 50Mo de mémoire à une image disk :\
`fallocate -l 50M /tmp/disk.img`

Vérification que le fichier a bien été créé et qu'il fait bien 50Mo :\
`stat /tmp/disk.img `

Création du système de fichier au sein du fichier image disque que nosu avons créé :\
`/sbin/mkfs.fat /tmp/disk.img`

Création d'un fichier de périphérique loop que l'on va pouvoir utiliser pour pouvoir accéder au contenu du système de fichiers de ce fichier image (en gros on map le fichier en pseudo périphérique) :\
`udisksctl loop-setup -f /tmp/disk.img`

Pour finir on monte l'image de disk :
`udisksctl mount -b /dev/loop0 `

Resultat : `Mounted /dev/loop0 at /media/mocafrain/af8a6498-e6c2-4c6e-ac22-de859814f36d` --> On peut désormais accéder à notre système de fichier depuis cette endroit `cd media/mocafrain/af8a6498-e6c2-4c6e-ac22-de859814f36d`
