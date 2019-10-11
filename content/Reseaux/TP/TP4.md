---
title: "TP4 Le Protocole HTTP"
date: 2019-10-11T14:06:45+02:00
draft: false
---
http://dept-info.labri.fr/~thibault/Reseau/TP4.pdf

# Une première utilisation de telnet

Quel est l’effet de la commande suivante ? `telnet time-c.nist.gov daytime`

```bash
mocafrain@saaz:~$ telnet time-c.nist.gov daytime
Trying 129.6.15.30...
Connected to time-c-g.nist.gov.
Escape character is '^]'.

58767 19-10-11 13:08:10 24 0 0 179.7 UTC(NIST) *
Connection closed by foreign host.

```

Pour le wikipedia du protocole daytime il est dit que :

```
The Daytime Protocol is a service in the Internet Protocol Suite, defined in 1983 in RFC 867. It is intended for testing and measurement purposes in computer networks.

A host may connect to a server that supports the Daytime Protocol on either Transmission Control Protocol (TCP) or User Datagram Protocol (UDP) port 13. The server returns an ASCII character string of the current date and time in an unspecified format.
```

En gros le retour `58767 19-10-11 13:08:10 24 0 0 179.7 UTC(NIST) *` est une chaine de caractère ASCII retournée par le serveur précisant la date et l'heure.

# Protocole HTTP

## Méthode GET simple et entêtes

Le port utilisé par HTTP est le port `80`.

`GET http://bruno.pinaud.emi.u-bordeaux.fr/test-redir`

```
mocafrain@saaz:~$ telnet bruno.pinaud.emi.u-bordeaux.fr 80
Trying 2001:660:6101:800:252::9...
Connected to pagesperso.emi.u-bordeaux.fr.
Escape character is '^]'.
GET http://bruno.pinaud.emi.u-bordeaux.fr/test-redir
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://www.u-bordeaux.fr">here</a>.</p>
</body></html>
Connection closed by foreign host.
```

## HTTP + ssl : HTTPS

`openssl s_client -connect www.truc.bidule.com:https.`

```bash
mocafrain@saaz:~$ openssl s_client -connect www.google.com:https
CONNECTED(00000003)
depth=2 OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
verify return:1
depth=1 C = US, O = Google Trust Services, CN = GTS CA 1O1
verify return:1
depth=0 C = US, ST = California, L = Mountain View, O = Google LLC, CN = www.google.com
verify return:1
---
Certificate chain
 0 s:/C=US/ST=California/L=Mountain View/O=Google LLC/CN=www.google.com
   i:/C=US/O=Google Trust Services/CN=GTS CA 1O1
 1 s:/C=US/O=Google Trust Services/CN=GTS CA 1O1
   i:/OU=GlobalSign Root CA - R2/O=GlobalSign/CN=GlobalSign
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFizCCBHOgAwIBAgIRALlsZlUHetawCAAAAAAU+18wDQYJKoZIhvcNAQELBQAw
QjELMAkGA1UEBhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczET
MBEGA1UEAxMKR1RTIENBIDFPMTAeFw0xOTA5MTcxMzI1NTBaFw0xOTEyMTAxMzI1
NTBaMGgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQH
Ew1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKEwpHb29nbGUgTExDMRcwFQYDVQQDEw53
d3cuZ29vZ2xlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMVy
psVp/juScYskP7M2bVXlTdzXahVVQIoR9e7RtrlCh5DVMEPzK/9WWHxutc8rO+HI
F7YgNZyGtEnGjtMC6N4sZ6z2O82PysSW4PF9Wl15IKJZB4hZ2VlqSAPKMMWzLFdP
0E6al0or9XvMMtoXfxSeXGNDBJ8asfYKhajzGgSdcKcPIrzS1gIiehmaHpjP4+QG
WsnNWsdFCcIT0Nh5+mQYs5xeB62rYK+799y5p6CMHa+HBtFfyVGTnq6afUtlyZIV
DJJ+b+kVxMpgunSsITvvcnejBhgPiY4c1z0rzm7953z6+kj7rKAPXDzOVXj49kTj
x8+3dFsVa1DvR4AMV2UCAwEAAaOCAlQwggJQMA4GA1UdDwEB/wQEAwIFoDATBgNV
HSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBRQUKJvhngv
bjCCffxdA9Qwbyr7uzAfBgNVHSMEGDAWgBSY0fhuEOvPm+xgnxiQG6DrfQn9KzBk
BggrBgEFBQcBAQRYMFYwJwYIKwYBBQUHMAGGG2h0dHA6Ly9vY3NwLnBraS5nb29n
L2d0czFvMTArBggrBgEFBQcwAoYfaHR0cDovL3BraS5nb29nL2dzcjIvR1RTMU8x
LmNydDAZBgNVHREEEjAQgg53d3cuZ29vZ2xlLmNvbTAhBgNVHSAEGjAYMAgGBmeB
DAECAjAMBgorBgEEAdZ5AgUDMC8GA1UdHwQoMCYwJKAioCCGHmh0dHA6Ly9jcmwu
cGtpLmdvb2cvR1RTMU8xLmNybDCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AGPy
283oO8wszwtyhCdXazOkjWF3j711pjixx2hUS9iNAAABbT+dg3EAAAQDAEcwRQIh
AM8q47CCM7yk+uduYuVoLDcBnZGgvTU/nwx0POI5S0MbAiBj+vQ3gW4pOVD5mkxQ
05Bxgja8jOUzO+E5VxjJ87Qx+wB2AHR+2oMxrTMQkSGcziVPQnDCv/1eQiAIxjc1
eeYQe8xWAAABbT+dg5oAAAQDAEcwRQIhAJ2ohO7q+DDDsQlA4fPPhs8x8iCSn/uX
YCvshYKIrEu9AiAGNbbPwJEjr9wpPgD8q3Lgv7B6w6Wkz8wbwDVRd62WMjANBgkq
hkiG9w0BAQsFAAOCAQEAnxzWZi37Q6bWeeSJVW535hUgYWskHCnQetl8F22xXQwL
+2vdPEBV9wKgFxyAgqGRR4fVWdsdh0osW7UuII9bkEAtViF3Aw5wkUnZ3V0EwCfU
oxvpd0IfOqbha2bh50iH6F4FDdu2kxkRvl0aFgIP5LYjF7gTMemXAraMA0ecvzmR
5Jdskck6Q2ZrVXqut0Tv0H2UEHHtwKygHQ+FMSOgkxOBs/JwpR9tNhE9/JsulrVP
ZvOA6NYd9F3Vkondc01YAcyobMLek8818qSznhmkqfdqDv/xkFsLoSkDEczO7Bbt
6R4/M70FtdL7iQYLEUgvXHMzYrMuwjOKvoEumWqgXw==
-----END CERTIFICATE-----
subject=/C=US/ST=California/L=Mountain View/O=Google LLC/CN=www.google.com
issuer=/C=US/O=Google Trust Services/CN=GTS CA 1O1
---
No client certificate CA names sent
Peer signing digest: SHA256
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 3201 bytes and written 261 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-CHACHA20-POLY1305
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-CHACHA20-POLY1305
    Session-ID: 5F29331CCBBB8532FB7E454C2B051C6ADDB18E60E91FEA34F07A982AAA4282C4
    Session-ID-ctx:
    Master-Key: EAF73A56B0C55B312E894AE7E42B8A56E701DFC6C841600D79C892C141251886320001F54CBB45F72DB46A6E2410F40D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 100800 (seconds)
    TLS session ticket:
    0000 - 00 02 43 c8 2c a9 5e bf-e7 3c 3e 27 41 8a 61 3b   ..C.,.^..<>'A.a;
    0010 - ba c2 e1 5a ff 11 37 ec-20 e0 cf 8e 61 29 71 e1   ...Z..7. ...a)q.
    0020 - 5f e1 3b 05 f3 be 4b 8c-77 a9 b1 83 bc 05 93 7c   _.;...K.w......|
    0030 - 60 dd 93 20 ef fa 56 87-67 13 ca 73 87 2e b4 f0   `.. ..V.g..s....
    0040 - c7 21 7d a8 3a 1e 30 bd-36 ee 08 f4 6e d1 26 a1   .!}.:.0.6...n.&.
    0050 - f0 e3 f9 1c 05 1f d7 f8-33 b3 df 62 9f c3 b1 ea   ........3..b....
    0060 - 08 36 b0 7e bb a7 04 ac-d1 a6 4a 12 ee 58 98 cf   .6.~......J..X..
    0070 - f2 49 22 82 03 3b 2d b4-58 ee 1d 27 a2 59 d6 fa   .I"..;-.X..'.Y..
    0080 - 06 0f 55 a8 9f c7 c4 55-d3 f2 ba da ab 6a c1 eb   ..U....U.....j..
    0090 - ff 55 9f dd a9 40 17 22-1c 78 73 e5 29 85 27 74   .U...@.".xs.).'t
    00a0 - 69 2a f8 60 c6 cf 72 29-4d 57 69 05 45 7a c3 9d   i*.`..r)MWi.Ez..
    00b0 - 12 fa cc 9f 45 fb 4d 7b-8c 25 20 dc 80 bd 40 31   ....E.M{.% ...@1
    00c0 - 10 fb d0 57 9f ef 74 26-91 b3 d7 11 33 7e 9b dd   ...W..t&....3~..
    00d0 - 09 db 3e 24 96 45 fa 1a-69 0d                     ..>$.E..i.

    Start Time: 1570801857
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
---

```

# Cookies et formulaires

`sqlitebrowser $HOME/.mozilla/firefox/*.default/cookies.sqlite`

Résultat après avoir completé le formulaire :

ID | baseDomain | originAttributes | name | valu | host | path | expiry | lastAccessed | creationtime |
---|------------|------------------|------|------|------|------|--------|--------------|--------------|
683|u-bordeaux.fr| | fruit | Fruix | samuel.thibault.emi.u-bordeaux.fr | / | 1570802504 | 1570802444581248 | 1570802444581248 |

# Vraiment à la main

[Lien du script `httpget.py`](/Reseaux/TP/scripts/httpget.py)
