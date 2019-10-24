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

<u>Configuration de slapd</u> :

+ No pour la première question afin de pouvoir utiliser l’outil de configuration
+ pour nom DNS : mon-entreprise.com
+ pour nom d’organisation : mon-entreprise
+ le mot de passe administrateur x2
+ choisissez le format de base par défaut : mdb
+ No pour savoir si la base doit être supprimée quand slapd est purgé
+ Yes pour déplacer l’ancienne base de données

```
Config perso :
dc=entreprise,dc=com
admin : mdpadmin
```
### Gestion de l'annuaire

La gestion de notre LDAP se fera avec ***APACHE DIRECTORY STUDIO*** (https://directory.apache.org/studio/)

Nous allons créé une nouvelle connexion avec nos paramètres :

+ Hostname : 127.0.0.1
+ Port : 389
+ Bind DN ou nom d'utilisateur (SASL) : cn=admin,dc=entreprise,dc=com
+ MDP : mdpadmin

Pour cette connexion, nous allons ensuite créer de nouvelles entrées, soit les dmdName : users, machines et roles.

La configuration et l'arborescence sera de la forme suivante :

![Config_et_arborescence](/Installation/Elineau/TPLDAP_ressources/arbor_dmd.png)

Au préalable avant d'installer le PAM LDAP, j'ai créé deux utilisateurs de la forme suivante :

![Config_user](/Installation/Elineau/TPLDAP_ressources/config_user.png)

## PAM LDAP

<u>PAM</u> : Pluggable Authentification Module. Cela va nous permettre d'ajouter des modules au service d'authentification de Debian.\
Plus précisement, ça va nous être utile pour creer comptes utilisateurs sur les systèmes UNIX pour chaque compte (objectClass : posixAccount) de notre LDAP.

### Installation

> https://wiki.debian.org/fr/LDAP/PAM /!\ La config précisé ici peut faire planter le système d'authentification /!\

> Paquet à installer : libpam-ldap & libnss-ldap

+ `apt install libpam-ldap libnss-ldap`

+ Compte de l'administrateur/root LDAP : `cn=admin,dc=entreprise,dc=com` | `mdp: mdpadmin`.

### Configuration

D'abord **configurons le fichier** `/etc/nsswitch.conf` :

```
passwd:         files ldap
group:          files ldap
shadow:         files ldap
```

Ici nous précisons les fichiers à utiliser pour l'authentification.

Ensuite dans le fichier `/etc/libnss-ldap.conf` nous allons **verifier la bonne configuration de l'URI et de la "base"** (que vous avez probablement dû configurer à l'installation) :

```bash
uri ldap://127.0.0.1/
base dc=entreprise,dc=com
```

Pour finir nous allons **rajouter une ligne au fichier** `/etc/pam.d/common-account` permettant de faire en sorte que des repertoires personnel soit creer pour chaque nouvelle utilisateur loggé :

```
session         required        pam_mkhomedir.so skel=/etc/skel umask=0022
```

On **redémarre ensuite le service nscd** :

```bash
systemctl restart nscd
```

Et on **vérifie la présence de nos utilisateurs** avec la commande :

```bash
getent passwd
```

## POSTFIX

> Paquet à installer : postfix

```
apt install postfix
```

Si vous n'avez pas la commande `mail` :
```
apt install mailutils
```


______

# Correction

Jusqu'à présent :

1. Install LDAP
2. Mise en oeuvre de cette annuaire | IHM LDAP
3. PAM LDAP
4. POSTFIX
5. Liaison POSTFIX LDAP
6. SAMBA
7. Relier SAMBA et LDAP

### Install LDAP

```
apt-get install ldaputils slapd
```

### Mise ne oeuvre de cette annuaire
apache directory studio, ou (logiciel présent sur les dépôts Debian)

> il est bien de creer un conteneur `dmdName=Roles` pour toute l'organisation hierarchique de l'entreprise.

### PAM LDAP
Verifier branche dmdName=People avec :

+ Attributs :
  + uidNumber : Essayer de commencer à 1001 pour eviter les conflits avec les services. Et pas le même gid entre les utilisateurs.
  + gidNumber : Idem.
  + homeDirectory = /home/toto
  + UserPassword


+ Class :
  + posixAccount
  + shadowAccount
  + person
  + et un dernier dont il ne se souvient plus.

> La classe d'objet extensibleObject permet de passer outre les violations.

> Le PAM quand il est configuré dans notre interet va détourner le principe d'authentification pour le pas utiliser par défaut le fichier `/etc/passwd` mais le LDAP.

Fichiers à config :

+ /etc/nsswitch.conf
+ /etc/libnss-ldap.conf
+ /etc/pam.d/

### POSTFIX

> Quand POSTFIX envoie un message, il tague ce message (identifiant unique).

> /var/spool/rsyslog/

Le LDAP permet de gerer toutes les problèmatiques de LD. Grâce à des valeurs comme groupofname et ...

Le petit script à mettre ne oeuvre pour que le POSTFIX soit capable de le traiter. Il se compose de 6 lignes. la premiere pour faire appel au serveur d'annuaire, la deuxieme pour le port, la troisieme on lui met la base de recherche (a quel endroit tu vas chercher recursivement), il faut lui donner le compte qui à les droits d'admin (eg : cn=admin,[...]), ensuite on lui met le query filter permettant de définir des filtres pour choisir les utilisateurs en fonction des paramètres passés.

```bash
root@debian:/etc/postfix# telnet localhost 25
Trying ::1...
Connected to localhost.
Escape character is '^]'.
220 debian.entreprise.com ESMTP Postfix (Debian/GNU)
test
502 5.5.2 Error: command not recognized
mail from: test@entreprise.com
250 2.1.0 Ok
data
554 5.5.1 Error: no valid recipients
mail
503 5.5.1 Error: nested MAIL command
mail from: maxime.ocafrain@entreprise.com
503 5.5.1 Error: nested MAIL command
rcpt to: maxime.ocafrain@entreprise.com
550 5.1.1 <maxime.ocafrain@entreprise.com>: Recipient address rejected: entreprise.com
rcpt to:maxime.ocafrain@localhost
250 2.1.5 Ok
data
354 End data with <CR><LF>.<CR><LF>
To:maxime.ocafrain@entreprise.com
From:admin@enteprise.com
Subject: Test SMTP
Ceci est un test d'envoie de courriel via notre serveur SMTP

```
// A trier

Penser à installer `apt install postfix-ldap`

Création d'un fichier de config pour les utilisateurs du ldap dans `/etc/postfix/` :

```bash
server_host = ldap://127.0.0.1/
search_base = dmdName=users,dc=entreprise,dc=com
bind = yes
bind_dn = cn=admin,dc=entreprise,dc=com
bind_pw = mdpadmin
query_filter = (&(objectClass=organizationalPerson)(uid=%s))
result_attribute = uid
result_format = %s/
```

postfix reload

postmap -q maxime.ocafrain@entreprise.com ldap:/etc/postfix/ldap_users.cf

```bash
maxime.ocafrain@debian:~$ mail -s "Sujet de test" sarah.lu@debian.entreprise.com
Cc:
Voici un mail de test
```

```bash
"/var/mail/sarah.lu": 1 message 1 nouveau
>N   1 Maxime Ocafrain    jeu. oct. 17 10:  13/517   Sujet de test
?
Return-Path: <maxime.ocafrain@debian>
X-Original-To: sarah.lu@debian.entreprise.com
Delivered-To: sarah.lu@debian.entreprise.com
Received: by debian.entreprise.com (Postfix, from userid 2000)
	id 82867C0AA; Thu, 17 Oct 2019 10:29:16 +0200 (CEST)
Subject: Sujet de test
To: <sarah.lu@debian.entreprise.com>
X-Mailer: mail (GNU Mailutils 3.5)
Message-Id: <20191017082916.82867C0AA@debian.entreprise.com>
Date: Thu, 17 Oct 2019 10:29:16 +0200 (CEST)
From: Maxime Ocafrain <maxime.ocafrain@debian>

Voici un mail de test
```

### SAMBA LDAP

http://simon.crespeau.emi.u-bordeaux.fr/cours/adminsys/ldap/ldap-et-samba/

https://wiki.debian.org/LDAP/OpenLDAPSetup#For_SAMBA_LDAP_support
