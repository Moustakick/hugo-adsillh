ALTER TABLE Hotel.Reservation ADD CONSTRAINT DatesPossibles
  CHECK(Hotel.DatesCorrectes(idfacture,idChambre, date_debut, date_fin));
