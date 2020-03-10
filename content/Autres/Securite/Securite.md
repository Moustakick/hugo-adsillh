---
categories: ["Secu"]
title: "Sécurité"
date: 2020-01-14T13:52:51+02:00
draft: false
---
Enseignants :
+ André Lenoir\
Travail dans une startup qui s'appelle Tetris.
+ Jonathan Durant

Mail : lenoir.and@gmail.com, jonathan.durant@gmail.com

# Sécurité et sureté du SI
## Introduction et rappels

### Préambule

Installer KALI.

CVE : Common Vulnerabilities. Plus un produit a de CVE, plus c'est de la merde.

Idée de sécu : r/netsec, machine learning malware detection, Attaque de mitnick, honeypot...

D'ici 2 semaines, avoir choisi le sujet.

Calendrier :

+ 29 janvier : sujet choisi.
+ 12 février : Remise des plans.
+ 12 mars : Remise des rapports.
+ 25-26 mars : Exposés.
+ 26 mars : Challenge.
+ Exos Bonus.


# Authentification - PKI

## Identification vs Authentification vs Autorisation

Identification : Connaitre l'identité d'une entité.

Authentification : Vérifier cette entité.

Autorisation : Autoriser l'entité.

## Facteurs d'Authentification

+ Facteur mémoriel
  - C'est une information que j'ai mémorisé
      > mot de passe, nom de jeune fille de ma mère, code confidentiel, nom d'utilisateur, réponse à une question secrète, code pin.
+ Facteur matériel
  - Ce que je possède.
      > Clé USB, carte de puce, téléphone mobile, porte clé, etc...
+ Facteur corporel
  - Une caractèristique corporel que je possède.
      > balayage de la rétine, reconnaissance vocale, reconnaissance faciale, etc..
+ Facteur réactionnel: Ce que je fais
  - Signature
+ Facteur de lieu: Ou je me retrouve
  - GPS

## Méthode d'Authentification

+ Authentification simple
  - Ne repose que sur un facteur
  > ie : mot de passe uniquement
+ Authentification forte
  - repose sur au moins deux facteurs
  > ie : login + mdp + mot de passe généré (sur téléphone)
+ Authentification unique = SSO
  - Une seule authentification poru accéder à plusieurs applications.

## Mot de passe

graph TD
    L'utilisateur ne choisit pas toujours son moyen d'authentification. --> Mot de passe robuste

### De quoi dépend la robustesse d'un mot de passe ?

+ Compléxité du mot de passe
+ Mécanisme vérification (temps de vérification)
+ Modèle d'attaquant et moyens
+ Nombre authentification ratées autorisées
+ Mécanisme alertes

### Recommandation ANSSI

+ utiliser des mot de passes différents pour des systèmes distincts
+ Choisissez un mot de passe qui n'est pas lié à votre
+ Ne demandez jamais à un tiers de vous créer un mot de passe
+ Modifier systématiquement les mots de passe par défaut
+ Renouvelez vos mots de passe avec une fréquence raisonnable
+ Ne stockez pas vos mots de passe dans un fichier sur un poste exposé
+ Ne vous envoyez pas vos mots de passe sur votre messagerie personnelle
+ Configurer les logiciels et navigateurs pour qu'ils ne se souviennent pas des mot de passe saisi

### Règle simple de complexité

+ Au moins 12 caractères
+ Majuscules
+ Minuscules
+ Chiffres
+ Caractères spéciaux

### Logiciel

+ Générer mots de passe
+ Multi Devices
+ Remplissage auto
+ Protégé par authentification forte

Exemple de logiciel : KeePass, 1Password, LastPass...

### Protection des internautes : Sanction CNIL

+ 8 caractères
+ Au moins 3 types de caractères différents
+ Pas de lien avec un détenteur
+ Renouveler tout les 6 mois
+ Différents des mots de passe précédents

### Stockage des mots de passe dans les applis

voir diapo

## PKI

Public Key Insfrastructure

Une Insfrastructure à clé publique a pour objectif de gérer des clées et des certificats. La gestion des ces clés et certificats permet créer un environnement réseau de confiance.

graph TD
    A[PKI] --> B[certificats numériques]
    B --> C[Authentification]
    B --> D[Signature]
