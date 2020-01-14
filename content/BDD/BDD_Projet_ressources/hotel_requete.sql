-- une relation
SELECT * FROM Hotel.Chambre;

SELECT * FROM Hotel.Reservation R1, Hotel.Reservation R2;
SELECT * FROM Hotel.Reservation R1, Hotel.Reservation R2
WHERE R1.numero = R2.numero AND
  ((R1.date_debut > R2.date_debut AND R1.date_fin > R2.date_fin AND R1.date_debut < R2.date_fin) OR
  (R1.date_debut < R2.date_debut AND R1.date_fin < R2.date_fin AND R1.date_fin > R2.date_debut) OR
  (R1.date_debut > R2.date_debut AND R1.date_fin < R2.date_fin) OR
  (R1.date_debut < R2.date_debut AND R1.date_fin > R2.date_fin));

SELECT * FROM Hotel.Reservation R1, Hotel.Reservation R2
WHERE R1.numero = R2.numero AND
  ((R1.date_debut >= R2.date_fin) OR (R1.date_fin <= R2.date_debut));

SELECT * FROM Hotel.Reservation R1, Hotel.Reservation R2
WHERE R1.numero = R2.numero AND
  ((R1.date_debut > R2.date_fin) OR (R1.date_fin < R2.date_debut));

SELECT * FROM Hotel.Bar;

SELECT * FROM Hotel.Consommation;
