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

Dans les processus légers la communication via IPC n'ont pas grand intérêt car les processus léger partage le même emplacement mémoire, par conséquent partage les mêmes variables etc.

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

Il est intéressant de noter que la limite du nombre de threads est défini dans le fichier `/proc/sys/kernel/threads-max` et que malgré cela quand nous lançons le programme avec un nombre x de threads, l'allocation de mémoire ne se fait plus à partir de 32754 threads.

## Détacher un processus léger
`pthread_detach()`\
C'est une manière de terminer un processus leger, car une fois detacher il ne peux prendre fin tout seul.

## Identité d'un processus léger
Les identifiants d'un processus léger sont "masqués". Pour cela que la fonction  `pthread_self()` est utile, pour pouvoir afficher son identifiant.

La fonction `pthread_equal()` permet elle de savoir si deux thread sont différents.

## Section critique
Opération Atomique : L'idée derrière cette notion c'est qu'il s'agit d'une opération qui, comme la notion d'atome, est insécable. Par conséquent une opération atomique va être executé d'un bloc d'un seul.

Rappel à la notion de Mutex pour la gestion de ces sections critiques.

Dans le programme d'exemple : Nous avons deux fils d'executions qui partage la même variable. Si tout ce passe convenablement la valeur est incrémenté 100000000 de fois pour chaque thread. Donc le résultat devrait être 200000000 (ce qui n'est pas le cas).

## Les mutex
On peut associé le Mutex à un mécanisme de verrou entre les threads, cela permet notamment que deux threads n'ai pas accès a une section critique en même temps.

## Les variables conditions
Un mutex contrôle l'accès à une section critique. La variable condition est un petit peu différent.\
Elle permet à un processus léger d'informer ces pairs du changement d'une ressource partagée.

> Ex : telechargment dans un navigateur web. Pop-up avec le telechargement. A un moment le dl est fini. Pour afficher l'option indiquant que le dl est fini. Soit nous avons un mecanisme de scrutation, on va continuellement regardé pour voir si c'est fini. Soit nous avons un mecanisme d'avertissement, le thread va nous indiqué quand il a fini.

Ce mécanisme empêche par conséquent une consommation excessive de CPU que peut engendrer une mécanisme de scrutation.

Les variables de conditions sont sans états.

## Thread safe

---

Creation d'un programme `./prog_thread` qui ouvre un fichier `f`, et qui va lire un nombre de bloc limité `b` d'un taille donnée `s`.

`./prog_thread f b s`

On va ensuite faire un hash de chacun de ces blocs `xn`, on les concaténe et on fait un hash md5 de tout ça `x1 + x2 + x3 + ... + xn`.
