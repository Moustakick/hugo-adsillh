
/* CREATE TABLE Hotel.Chambre (
    numero serial NOT NULL,
    prix INTEGER NOT NULL CHECK (prix >=0),
    -- clef primaire
    PRIMARY KEY (numero)
); */

INSERT INTO Hotel.Chambre
  VALUES(DEFAULT,100);
INSERT INTO Hotel.Chambre
  VALUES(DEFAULT,125);
INSERT INTO Hotel.Chambre
  VALUES(DEFAULT,75);
INSERT INTO Hotel.Chambre
  VALUES(DEFAULT,50);
INSERT INTO Hotel.Chambre
  VALUES(DEFAULT,50);


INSERT INTO Hotel.Reservation
  VALUES(2, '2019-10-01', '2019-10-03');
INSERT INTO Hotel.Reservation
  VALUES(2, '2019-10-05', '2019-10-09');
INSERT INTO Hotel.Reservation
  VALUES(3, '2019-10-01', '2019-10-03');
INSERT INTO Hotel.Reservation
  VALUES(3, '2019-10-05', '2019-10-09');
-- Reservation en conflit/erreur :
INSERT INTO Hotel.Reservation
  VALUES(3, '2019-10-05', '2019-10-04');
INSERT INTO Hotel.Reservation
  VALUES(3, '2019-10-06', '2019-10-08');


INSERT INTO Hotel.Bar
  VALUES('Bière', 6);
INSERT INTO Hotel.Bar
  VALUES('Whisky', 8);
INSERT INTO Hotel.Bar
  VALUES('Coca', 3);

INSERT INTO Hotel.Consommation
  VALUES('Bière', 3, '2019-10-09');
INSERT INTO Hotel.Consommation
  VALUES('Whisky', 5, '2019-10-12');
INSERT INTO Hotel.Consommation
  VALUES('Coca', 75, '2019-10-2');
