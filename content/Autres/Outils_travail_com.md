---
title: "Outils de communication et travail"
date: 2019-09-30T13:52:51+02:00
draft: false
---
### Confiuration annexe :

+ Fenetre Term
+ Firefox

Firefox : dept-info.labri.fr/~delmas /enseignement/ → PDF

Lecteur de pdf utilisé pour Firefox : Okular

Extension : Flagfox (localisation et IP du siteweb), HTTPS Everywhere || avis perso : Privacy Badger.

___

### Configuration de messagerie électronique :

+ IMAP : webmel.u-bordeaux.fr 993
+ SMTP : smtpauth.u-bordeaux.fr 465

Configuration des news :\
  adresse mail etudiante

+ news.u-bordeaux.fr port563 ssl
+ S’abonner : local.test
  + Ecrire quelque chose au pif
+ S’abonner : licencepro.adshillh

Netiquette → coutume des news

___

### Connexion au réseau Eduroam :

+ TTLS
+ PAP
+ Certificat : domaine : radius.u-bordeaux.fr
+ identité : login@u-bordeaux.fr
+ anonyme : anonymous@u-bordeaux.fr
+ mdp : mdpetudiant

___

### Accès au Moodle :
ENT → plateforme pedagogique → science et technologies.  

___

### Travail à distance :

+ Connexion sur la machine passerelle "jaguar" :

```
ssh -Y ton_login@borderhost.emi.u-bordeaux.fr
```

+ Depuis la machine borderhost, se connecter à une machine de la liste de l'EMI https://services.emi.u-bordeaux.fr/nagios3/nagvis/nagvis/index.php (voir salle UC2) :

```
ssh -Y ton_login@nom_machine
```

NB : Il est possible d'allumer les PC depuis le site https://services.emi.u-bordeaux.fr/allservices/, rubrique "Le Démarrage à distance des pc dans les salles".\
Le "-Y" ou alors "-X" permet de gèrer les applications graphiques en ssh.s 
