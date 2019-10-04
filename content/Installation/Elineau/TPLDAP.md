---
title: "TP LDAP"
date: 2019-10-03T09:41:23+02:00
draft: false
---
# TP LDAP
Cours de Yorick : https://git.epha.se/ephase/cours_lpro-ADSILLH/src/branch/master/content/installations/TDM_1-OpenLDAP/index.md
## Gestionnaire d'annuaire
### Installation
Apache Directory Studio : https://directory.apache.org/studio/

### Creation d'un annuaire

> Creation d'un serveur (https://openclassrooms.com/fr/courses/1733551-gerez-votre-serveur-linux-et-ses-services/5236036-installez-un-annuaire-ldap) avec OpenLDAP `slapd`.

+ `sudo apt-get install slapd ldap-utils`
+ `sudo dpkg-reconfigure slapd`

```
Config perso :
dc=entreprise,dc=com
admin : mdpadmin
```
### Gestion de l'annuaire

> Ajout de nouvelles entrées, etc.

## PAM LDAP

<u>PAM</u> : Pluggable Authentification Module. En gros ça permet d'ajouter des modules au service d'authentification de Debian.

### Installation

> https://wiki.debian.org/fr/LDAP/PAM

> Paquet à installer : libpam-ldap

+ port 389
+ Compte de l'administrateur LDAP : `cn=admin,dc=entreprise,dc=com` | `mdp: mdpadmin`.
