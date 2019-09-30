---
title: "Les appels système"
date: 2019-09-30T12:06:02+02:00
draft: false
---
# Les appels système
## L’appel système open
Afin de manipuler un fichier il faut toujours commencer par ouvrir le fichier. Pour ce faire il existe l’appel système « open ».

> voir page de manuel de « open ».

Appel système qui ouvre le fichier identifiée par pathname et retourne un descripteur de fichier. En fonction de l’argument flags les fichier peut être ouvert en lecture et en écriture ou les 2. L’argument mode….\
L’argument flags de open est un masquage de bit qui spécifie le mode d’accès au fichier.

| Flags | Utilisation |
|:-------------|:-------------:|
| O_RDONLY     | Lecture seule |
| O_WRONLY     | Ecriture seule |  
| O_RDWR | Lecture et écriture |
| *... encore d'autres* | *sur les slides* |

L’argument de mode de open est un masquage de bit les droits si un nouveau fichier est créé (entre autres si O_CREAT est présent en flags). Cela correspond plus ou moins aux permissions sur un fichier (celles que l’on voit à droite avec la commande « ls -l »).

> Voir le tableau de Mode avec Octal.

Ex : `fd = open(« test.txt », O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR)`
→ Ouvre le fichier ou créer le fichier test.txt. Ouverture en lecture/ecriture. Seul le propriétaire peut lire et écrire le fichier..

> petit exemple pratique de la mise en œuvre sous python (slide)

<u>umask</u> : permet de définir un impact sur la permission du fichier. Avec un umask à 0, la permission du fichier va être définie à 0666. Un umask à 0022 (umask par défaut) défini la lecture uniquement par défaut aux autre utilisateurs.

## L’appel système read
Appel système qui lit au moins count octets depuis la zone mémoire pointée et les écrits dans le fichier référencé par le descripteur de fichier.

## L’appel système write
Appel système qui lit au moins count octets depuis la zone mémoire pointée et les écrits dans le fichier référencé par le descripteur de fichier.

## L’appel système close
Appel système qui libère le descripteur de fichier fd et toutes ressources allouées par le noyau qui lui sont associées.

> exemple en c et python (slides)

## L’appel système lseek1 (Déplacement dans un fichier)
Quand on lit ou ecrit dans un fichier il y a un curseur de fichier (file offset). Par défaut positionner au début du fichier. A chaque lecture ou ecriture le curseur bouge.

L’appel système lseek est un appel système qui a plusieurs fonctionnement. Si tout ce passe bien il renvoie le nouvel emplacement.

→ off_t lseek(int fd, off_t offset, int whence) :

  + offset : défini à combien d’octet déplacer le curseur.
  + whence : défini la position initiale du curseur (voir tableau).

# Fichiers à trous
Un fichier est dit « à trou » lorsque l’on écrit en dehors des limites du fichiers. (Par exemple : Si l’on déplace le curseur 1000 case après la fin du texte et que l’on écrit il se formera un trou).

Le PC va stocker les portions utiles du fichier mais ne va pas stocker l’espace vide (trou) d’un fichier. Il se le représente mais ne conserve pas.

> Script python permettant l’écriture d’un fichier à « trous » multiples. (slides)
