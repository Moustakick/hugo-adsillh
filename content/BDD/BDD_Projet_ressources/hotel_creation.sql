CREATE SCHEMA Hotel;
/* SET search_path TO Hotel, public;
CREATE TABLE Hotel.Client (
    nom text NOT NULL,
    mail text NOT NULL,
    mot_de_passe text NOT NULL,
    -- clef primaire
    PRIMARY KEY (mail)
    -- clefs étrangère
    FOREIGN KEY (numero_reservation) REFERENCES Hotel.Reservation(numero_reservation),
    FOREIGN KEY (numero_de_facture) REFERENCES Hotel.Facture(numero_de_facture),
    FOREIGN KEY (boisson) REFERENCES Hotel.Consommation(boisson)
); */
CREATE TABLE Hotel.Chambre (
    numero serial NOT NULL,
    prix INTEGER NOT NULL CHECK (prix >=0),
    -- clef primaire
    PRIMARY KEY (numero)
);
CREATE TABLE Hotel.Reservation (
    numero serial NOT NULL,
    date_debut DATE,
    date_fin DATE CHECK (date_fin > date_debut),
    -- clef primaire
    PRIMARY KEY (numero, date_fin),
    -- clefs étrangères
    FOREIGN KEY (numero) REFERENCES Hotel.Chambre(numero)
);
CREATE TABLE Hotel.Bar (
    boisson text NOT NULL,
    tarif INTEGER NOT NULL,
    -- clef primaire
    PRIMARY KEY (boisson)
);
CREATE TABLE Hotel.Consommation (
    boisson text NOT NULL,
    Quantite INTEGER NOT NULL,
    Date_conso DATE NOT NULL,
    -- clef primaire
    PRIMARY KEY (boisson, Date_conso),
    -- clefs étrangères
    FOREIGN KEY (boisson) REFERENCES Hotel.Bar(boisson)
);
/* CREATE TABLE Hotel.Facture (
    prix_nuite DOUBLE NOT NULL,
    prix_conso DOUBLE NOT NULL,
    date_reglement DATE NOT NULL,
    numero_de_facture INTEGER NOT NULL,
    -- clef primaire
    PRIMARY KEY (numero_de_facture)
);
 */
