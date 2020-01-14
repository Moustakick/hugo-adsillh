CREATE FUNCTION Hotel.DatesCorrectes(integer, integer, date, date)
  RETURNS boolean AS $$
SELECT NOT EXISTS (
  SELECT *
  FROM Hotel.Reservation
  WHERE $1 != idFacture
    AND $2 = idChambre
    AND $3 <= date_fin
    AND $4 >= date_debut)
$$ LANGUAGE SQL;
