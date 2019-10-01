---
title: "Les fichiers"
date: 2019-09-30T10:56:55+02:00
draft: false
---
# Les fichiers

Deux types de mémoire : mémoire vive (RAM) et mémoire morte (HDD, ROM, etc..) : deux types d’espace de stockage de fichiers.

<u>Fichier</u> : entité qui réside qqpart, réside sur une disposition logique qui permet d’acceuillir ce fichier. Souvent les fichier sont sotcker dans une structure hierarchique (système de fichier1). Définition simple : Un fichier est un suite d’information traduite de l’octet (une suite d’octet).\
Exemple avec un fichier :
![BORDEAUX](../Les_fichiers_ressources/Les_fichier_bordeaux.png)

En théorie un fichier sur lequel on écrit simplement BORDEAUX devrait peser 8octets. En pratique il en pèse 9 à cause du caractère de changement de ligne (« man ascii » → caractère 0x0A).

Sortie de la commande « hexdump -c < f.txt » :

![BORDEAUX\n](../Les_fichiers_ressources/Les_fichier_bordeaux_n.png)

Pour empecher lors de l’écriture l’ajout de retour à la ligne automatique on peut faire la commande : « echo -n BORDEAUX > f.txt ».

# Les fichiers sous UNIX
Philosophie d’UNIX : « Tout est fichier ».\
Les entrées/sorties sont symbolisées par des manipulation des fichiers.\
Descripteur de fichier (file descriptor, fd) : est un entier positif affecté par le noyau pour réferencer une fichier en cours d’utilisation.

+ Descripteur de fichier standard :

| Descripteur | Utilisation | Nom POSIX|
|:-------------|:-------------:|:-----:|
| 0     | Entrée standard |STDIN_FILENO|
| 1      | Sortie standard      |  STDOUT_FILENO |
| 2 | Sortie erreur      | STDERR_FILENO |

> Voir le diapo pour plus de détails

Par convention ces descripteur de fichiers sont directement ouvert au démarrage de la machine.
