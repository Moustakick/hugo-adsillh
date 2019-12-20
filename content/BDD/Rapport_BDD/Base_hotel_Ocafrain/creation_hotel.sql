CREATE SCHEMA Hotel;
SET search_path TO Hotel, public;

CREATE TABLE Hotel.Client (
  idClient serial NOT NULL,
  nom text NOT NULL,
  prenom text NOT NULL,
  mail text NOT NULL,
  password text NOT NULL,

  PRIMARY KEY (idClient),
  UNIQUE (mail)
);

CREATE TABLE Hotel.Bar (
  boisson text NOT NULL,
  prix integer NOT NULL CHECK (prix > 0),

  PRIMARY KEY (boisson)
);

CREATE TABLE Hotel.Chambre (
  idChambre serial NOT NULL,
  tarif integer NOT NULL CHECK (tarif > 0),

  PRIMARY KEY (idChambre)
);

CREATE TABLE Hotel.Reservation (
  idFacture serial NOT NULL,
  idClient serial NOT NULL,
  idChambre serial NOT NULL,
  date_debut date NOT NULL,
  date_fin date NOT NULL,
  reglee boolean NOT NULL,
  date_reglement date NOT NULL DEFAULT 'epoch',

  PRIMARY KEY (idFacture),
  UNIQUE (idClient, idChambre, date_debut),
  UNIQUE (idClient, idChambre, date_fin),

  FOREIGN KEY (idChambre) REFERENCES Hotel.Chambre(idChambre),
  FOREIGN KEY (idClient) REFERENCES Hotel.Client(idClient),


  CHECK (date_debut < date_fin),
  CHECK ((not reglee) or (date_reglement>=date_fin))
);
CREATE TABLE Hotel.Consommation (
  idChambre serial NOT NULL,
  jour date NOT NULL,
  boisson text NOT NULL,
  quantite integer NOT NULL CHECK (quantite > 0),

  PRIMARY KEY (idChambre, jour, boisson),

  FOREIGN KEY (idChambre) REFERENCES Hotel.Chambre(idChambre),
  FOREIGN KEY (boisson) REFERENCES Hotel.Bar(boisson)
);
