---
title: "NTP"
date: 2019-09-26T11:22:50+02:00
draft: false
---
# Le protocole NTP
Cours sur le protocole NTP Network Time Protocol.\
<u>Enseignant</u> : Catarina Christophe

## Synchronisation des horloges
Les machines ont besoins d'horodatés (mettre des timestamp) à un moment pour pouvoir se synchroniser dans l'immédiat, pour des utilisations futur ou autres.\
L'écoulement du temps et sa mesure est quelque chose d'arbitraire.\
Cependant nous avons besoin de ça pour pouvoir parler pour pouvoir parler de la même chose. C'est pourquoi il existe le protocole NTP. Il est basé sur la base temps **UTC**.

## Généralités
Le protocole NTP est meilleur que le "Time Protocol" avec une precision supérieur à la seconde.
Le protocole NTP est actuellement en version 3.
LA RFC 1305 nous donne :
+ la description du protocole réseau
+ les modes de fonctionnement
+ les algorithmes à mettre en place dans les machines.

> Problème : le temps de demander l'heure et de la recevoir, l'heure n'est plus la même. Par conséquent des algorithmes ont été dev à chaque version de NTP afin d'améliorer la Synchronisation.\
 Ce protocole par conséquent ne permet pas de garantir l'heure EXACT. Cependant il permet en dessa d'être synchronisé avec les machine avec lesquels on communique.

 Une variante existante est SNTP, qui est une variante légérement plus simple (tiré de la version 3 de NTP) qui permet de se cantonner à des version utilisation plus simples.

## Principes
NTP comprend :

+ Une partie architecture : Le protocole se base sur une architecture mondial.
+
+

### Partie architecture
Arborescence classique : piramidale hierarchique. Des chefs qui donne l'heure au subordonnées qui distribue à d'autres etc.. Il y a que au niveau 1 de l'arborescence que la machine n'est pas cliente.\
Les horloges du plus haut niveaux se base sur des serveurs dit **primaires** qui se trouvent au plus près de l'horloge de références (Pour avoir le maximum de précisions).

***Voir schèma de l'arborescence***

> Une horloge temps réel n'est pas que méchanique mais aussi physique: exemple avec horloge atomique (changement de couches atomiques).\
> Sur le schèma le protocole ne commence qu'à la couche 2. Avant le lien est *physique*.

<u>Configuration du système</u> : Chaque noeud de cette archi doit être configuré. Il doit être défini s'il s'agit d'un serveur parent, enfant. Il doit être défini qui on a au dessus, qui on a à côté et très peu qui on a en dessous.\
L'architecture est dites *fléxible, extensible et robuste* car il peut se baser sur toutes les machines autours pour fonctionner : entre-aide entre machines etc..

Deux types de messages : messages de demande (client) et messages d'envoie (serveur).

Le mode d'adressage est unicast : on peut choisir les personnes ou la quantité de personnes à qui on peut parler.

#### Méthode pour la diffusion de l'heure
Tout le monde peut donner l'heure mais deux ne peuvent pas entre-communiquer en même temps. Par conséquent le système se base sur un paradigme du type "symétrique ACTIF/PASSIF" pour la diffusion latéral.

> L'essentiel n'est pas d'avoir l'heure exact mais une heure commune entre les machines

Il y a aussi un paradigme du type "broadcast" : une machine peut demander l'heure en broadcast et obtenir une réponse de plusieurs serveurs.

### Partie algorithmie
L'algorithmes NTP prévoit pour chaque client des méthodes :

+ Pour calculer la période d'interrogation du ou des serveurs.
+ Pour calculer l'écart de son heure locale avec celle d'un serveur donnée.
+ Pour calculer la durée de transit des messages sur le réseau.
+ Pour choisir le serveur qui présent les meilleures garanties de qualité, et calculer ainsi son stratum local.
+ Pour filtrer les écarts et calculer les corrections temps/fréquence à appliquer sur son horloge locale.
+ pour gérer les secondes intercalaires : passer d'un heure x à un heure x+n se fait de manière progressive. Ce réglage se fait dans la config de l'AdminSys.

## Architecture
*Voir la notion de strate sur la diapo avec le schèma.*
> On utilise de plus en plus de GPS pour avoir l'heure.

## Description détaillée du "fonctionnement NTP"
*Voir diapo avec la partie paquet*

## Ce que ne fait pas NTP
L'heure de référence fournie par NTP est UTC par conséquent il ne se charge pas :

+ du changement de l'heure dû au fuseau horaire.
+ du passage à l'heure d'été et d'hiver.

Les messages de NTP passe en clair.

## Installation du service NTP
<u>Partie configuration "tutoriel".</u>

> Les machines qui gère le mieux l'heure sont les téléphones portable. Les fuseaux sont gérés grâce au système de géoloc ou cellulaire.

Le système de pile de kapa? et de quartz permet de conserver le temps quand la machine est hors-ligne. Quand le système se remet en ligne les système se re-qualibre progressivement.\
NTPD n'est pas un service qui met à l'heure.

Fichier de configuration : `/etc/ntp.conf`. *Voir la "forme" de la config sur la diapo*.

Commandes utiles :

+ verification du serveur de référence :

```bash
ntpq -p
```

+ Miaou
