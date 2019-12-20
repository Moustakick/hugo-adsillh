ALTER TABLE Hotel.Reservation ADD CONSTRAINT DatesPossibles
  CHECK(Hotel.DatesDebutFinCorrectes(numero, date_debut, date_fin))
