CREATE VIEW Hotel.Facture AS SELECT idFacture, nom, prenom, mail, ((date_fin - date_debut)*tarif) AS Nuitees, sum(quantite * prix) AS Total
FROM Hotel.Chambre NATURAL JOIN Hotel.Reservation NATURAL JOIN Hotel.Consommation NATURAL JOIN Hotel.Bar NATURAL JOIN Hotel.Client
WHERE date_debut <= jour AND
      jour < date_fin
GROUP BY idFacture, nom, prenom, mail, date_debut, date_fin, tarif;
