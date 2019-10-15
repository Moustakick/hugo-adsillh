---
title: "Les tubes"
date: 2019-10-01T14:16:36+02:00
draft: false
---
https://openics.org/teaching/adsillh/06_Les-tubes.pdf

# Les tubes (pipe)

Mécanisme permettant au processus de dialoguer entre eux.

## Les tubes dans un shell

Le caractère pipeline `|` permet dans un shell d'utiliser les tubes.

> Pagination avec `less` de la sortie de la commande `ps faux` :

```shell
ps faux | less
```

```shell
ps faux |
```

Le pipe génère un flux, qui va servir d'entrée à la commande suivante, etc.

Les tubes sont un mécanisme qui sont gérés directement par le noyau. C'est un mécanisme normé par la norme POSIX.\
Les tubes passent par un appel systèmes pour leurs fonctionnement.

En fonction de la quantité  d'information passés, le noyau va remplir un tableau de descripteurs de fichiers.

p = [3|4] --> tableau de deux entiers\
p[0] = 3  --> STDIN\
p[1] = 4  --> STDOUT

Les tubes sont un moyen de communication dit HALF-DUPLEX, c'est à dire que la communication ne se fait que dans un sens.\
On écrit dans un sens et on reçoit les données dans l'autre sens.

Pour communiquer dans l'autre sens il faudrait créer un second pipe. Ensuite on fork pour faire une "copie" des données.
