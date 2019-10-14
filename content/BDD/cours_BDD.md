---
title: "Cours de BDD"
date: 2019-09-25T14:16:19+02:00
draft: false
---
Alain Griffault : alain.griffault@u-bordeaux.fr
Transparents : `cp ~ algriffa/LPro_BD/2019-2020/*pdf`

<!-- TOC -->

- [Cours 09/09/19](#cours-090919)
- [Cours 16/09/19](#cours-160919)
  - [Processus de construction d’une BD :](#processus-de-construction-dune-bd%C2%A0)
  - [Schéma relationel :](#sch%C3%A9ma-relationel%C2%A0)
  - [Concept de base : base de données](#concept-de-base%C2%A0-base-de-donn%C3%A9es)
- [Cours 23/09/19](#cours-230919)
  - [Le modèle entités-associations](#le-mod%C3%A8le-entit%C3%A9s-associations)
    - [Principe de base](#principe-de-base)
    - [Les types d’entités](#les-types-dentit%C3%A9s)
    - [Contraintes de cardinalités](#contraintes-de-cardinalit%C3%A9s)
- [Algèbre relationnelle](#alg%C3%A8bre-relationnelle)
  - [L'opérateur de projection](#lop%C3%A9rateur-de-projection)
  - [L'opérateur de selection](#lop%C3%A9rateur-de-selection)
    - [Exemple](#exemple)
  - [L'opérateur de jointure](#lop%C3%A9rateur-de-jointure)
    - [Exemple](#exemple-1)

<!-- /TOC -->

# Cours 09/09/19

Application WEB : Appli client serveur qui s’execute via un navigateur web. Ne sont pas comme une application de programmation, elles uttilisent divers langage différents (Code source hétérogène). HTML, CSS, PHP, SQL, JS, Java, ActiveX, Python,….\
Avantages : Déploiement facile car utilise en général peu de ressources coté client.\
Inconvénients : interfaces pauvres, nécessite un réseau et une infrastructure serveur solide.\
Trois grands types d’applications :

+ Les applications statiques. ex : Wikipedia.
+ Applications dynamiques côté serveur. Ex : Les moteurs de recherche.
+ Les applications dynamiques côté serveur et client. Ex : les sites de ventes.

Principe :

+ Statique : Requete du client → Réponse du serveur (page html, css…) → Affichage de la réponse côté client.
+ Dynamique : Requete paramétrée du client → Calcul de la réponse côté serveur par exécution du programmes → Réponse du serveur (page html, css ,…) → Affichage de la réponse côté client.
+ Dynamique des deux côtés :
Requetes paramétrée du client → Calcul de la réponse → Réponse du serveur : une page html+code, des directives css → interprétation du code côté client vers html → Afficahge de la réponse complétée côté client.

Projet hôtel : \
Trois modules distinct :

+ Un momdule SGBDR : Les clients, les reservations, les consommations et les factures seront gérés par une base PostgreSQL.
+ Un module ProgWeb : L’application web sera réalisée en python avec le momdule flask.
+ Une module NoSQL : Les descriptof de l’hôtel et des chambres ainsi que les avis seront réalisés avec un base mongodb.

Modalités :
+ Projet individuel.
+ Les trois modules feront l’objet de rapports distincts.

<u> Programmes</u> :\
*notions de base de SQL*\
SQL : un langage ***prédicatif***

```
+ Le modèle relationnel.
+ Qualités et défauts d’un schéma relationnel.
+ Dépendance Fonctionnelles modèle Entité-Association.
+ SQL : langage de description de schémas.
+ L’algèbre realtionnelle. Et SQL : un langage algébrique.
+ Extensions SQL.
+ Optimisation des bases de données.
```
Idée du projet : http://alain.griffault.emi.u-bordeaux.fr/flask/

Définition : SGBD \

+ SGBD : Système de Gestion de Bases de Données (parfois SGBDR pour Relationnel).
+ DBMS : Database Management System (parfois RDBMS)
+ Outil informatique pour gérer des BD.
+ Doit absolument posséder plusieurs fonctionnalités.
    + Sauvegarde des données.
    + Interrogation des données.
    + Recherche et mise en forme des données stockées.
    + Partage des données entre les différents utilisateurs.
    + Gestion de la concurrence d’accès.
    + Sécurité des données (gestion des incidents).
    + Optimisation des opérations dans une souci constant de performance.

# Cours 16/09/19
## Processus de construction d’une BD :

+ La partie du monde réel est décrite par des données et des contraintes
+ Ces données et contraintes sont formalisées dasn uns schéma modèle
+ Modèle entité relation.

## Schéma relationel :
+ Domaine: un ensemble de valeurs atomique (non décomposable, un tout)
    + entier, réel, caractère, bool etc..
    + Enumération finie. Couleurs = {bleu, blanc, rouge}
+ Problème des types structurés
    + Date de naissance, numéro INSEE... :Est-ce un objet simple ou complexe. Par exemple la date de naissance 16/09/19 peut être une valeur décomposable mais est traitée comme non décomposable (atomique).
    + Chaine de caractères. Idem.
+ Produit cartésien : Soit un ensemble de domaines D1, … ,Dn. Le produit cartésien noté D1*...*Dn est l’ensemble des n-uplets (tuples, vecteurs) <v1, … , vn> tels que [voir diapo].
    + On prend au moins deux objets et on les associes de toutes les manières possibles (toutes les combinaisons possibles)
+ Relation : Une relation est un sous ensemble des produits cartésiens. Ex : le drapeau hollandais et le drapeau francais, le domaine des couleurs * positions est similaire mais les sous ensembles sont différents.
    + Terminologie :
        + Un attribut, nom donnée à une colonne est composé d’un identifiant et d’un domaine.
        + Le degré d’une relation est le nombre d’attributs. Il est fixe.
        + Un n-uplet (tuple) est un élément de la relation. Il correspond à une logne de la table.
        + La cardinalité est le nombre d’éléments (lignes) de la realtion. Il est variable.
        + Exemple drapeau hollandais :
            + Les attributs :
                + CH : Couleurs
                + PH : Position
            + Degré : 2
            + Cardinalité : 3
+ Contrainte d’une relation
    + Soit un attribut A:D. Une contrainte de domaine sur l’attribut est un prédicat qui défini les seules valeurs possibles.
        + Exemple : soit une attribut NumeroMois:Entier. 1 =< NumeroMois =< 12
    + Une contrainte statique sur v est un prédicat sur D1* … *Dn qui défini les seules valeurs possibles pour v.
        + Exemple : mois en 31 et en 30, la valeur max des jours dépend de la valeur du mois.
    + Une contrainte sur r est un prédicat sur D1* … *Dn qui défini les seules sous-ensembles de tuples possibles pour r.

## Concept de base : schéma de relation

Définition :
+ Un schéma de relation R est défini par un ensemble d’attributs U et un ensemble de contraintes.
+ On le note couramment R(U)
+ Le schéma R(U) (attributs et contraintes) décrit l’intention de la relation.
+ La relation définit un extension.
+ Une relation r est une instance finie d’un schéma de relation notée r:R(U)

***Exemple de schéma de relation*** :\
+ Aliment préférés (nom, type, origine, bio)\
+ Régime Alimentaire (aliment, calories)\

## Concept de base : base de données
Définition :
+ Un schéma de base de données est un ensemble de realtions liés par des dépendances référentielles (un type de contraintes) : attributs communs ou plus généralement des dépendances d’inclusion.
+ Une base de données est alors un ensemble de raltions (extensions) associé au schéma de base de données et vérifiant toutes ses contraintes.

Un mauvais exemple :\
	Objectif : modélisation d’un compagnie aérienne. On veut savoir quel est l’avion utilisé pour 	chaque ligne et sa capacité. [voir diapo]\

  1. Espace de stockage : on apprend 4 fois que l’A330 a une capacité de 335 passagers
  2. Problèmes de mise à jour : changement de la capacité des avions ? Changement de type sur un vol ?
  3. Problème d’insertion : incoherence en cas d’introduction d’un A330 avec une capacité de 300. Introduction d’un nouveau type d’avion sans le faire voler ?
  4. Problème de suppression : suppression de IT5035, supprime le type Canadair.

# Cours 23/09/19
## Le modèle entités-associations
### Principe de base
Une manière d’obtenir un modèle relationnel, une forme d’intermediaire.
### Les types d’entités
Liés les entités (maison, personne) par un relation (Achète..).\
Cas particulier : Une entité peuvent êtres liés à elle même.
### Contraintes de cardinalités
Combien d’assocaitions pouvons nous lier à travers (R).\
Ne pas lire ces diagrammes comme un UML Diagramme de classe.\
*TRANSPARENT* : /net/cremi/algriffa/LPro_BD/2019-2020\
Accès au cours :`cp ~ algriffa/LPro_BD/2019-2020/*pdf`

# Algèbre relationnelle

>  Comment interroger une base de donnée en faisant de l'algèbre relationnelle.\
SQL est de l'algèbre relationnelle.

Cela va permettre de créer de nouvelle relation à partir de relation (Base théorique du langage SQL)

## L'opérateur de projection

> Noté pi

En algèbre on défini une relation R.\
En SQL la requête qui correspond est :

```SQL
SELECT * FROM R;
```
> Cela affiche tout le contenu de R


Pour le calcul dans R(A,B,C,D) (Diapo) :

C et D est affiché en supprimant les doublons.

Pour cette expression algébrique la requête SQL correspondante est :

```SQL
SELECT DISTINCT C,D FROM R;
```

> L'opérateur DISTINCT permet de ne pas affiché les doublons parmis les n-uplets des attributs.

Si je fait la même projection pour A,B que pour C,D il n'y aura pas de doublons du coup l'algorithme sera linéaire.

## L'opérateur de selection

> Noté sigma

Avec cette opérateur nous allons pouvoir définir un prédicat (partition horizontal) (ex : 'C>2' voir diapo).

### Exemple

```SQL
SELECT num_serie FROM Avion WHERE capacite>150
```

## L'opérateur de jointure

> Noté zboui

Cela permet de lier deux tables qui disposent d'un attribut logique commun.

### Exemple

> Nom de la personne qui consomme des crêpes ?

Dans cette exemple l'attribut commun est l'ID. En SQL pour  la table "consommation" il s'agit d'une clé étrangère et pour la table "client" il s'agit de sa clé primaire.

La requête SQL correspondant à l'exemple est :

```SQL
SELECT * FROM RI NATURAL JOIN R2
```
![](cours_BDD-80d84.png)

## Opérations binaires
