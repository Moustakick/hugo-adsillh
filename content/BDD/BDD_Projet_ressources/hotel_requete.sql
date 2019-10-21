-- une relation
SELECT * FROM Hotel.Chambre;

SELECT * FROM Hotel.Reservation R1, Hotel.Reservation R2;
SELECT * FROM R1 WHERE R1.date_fin > R2.date_debut AND R1.date_fin < R2.date_fin;

SELECT * FROM Hotel.Bar;

SELECT * FROM Hotel.Consommation;
