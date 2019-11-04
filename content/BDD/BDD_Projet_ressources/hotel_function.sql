CREATE FUNCTION Hotel.DatesDebutFinCorrectes(integer, date, date)
  RETURNS boolean AS $$
SELECT NOT EXISTS (
  SELECT *
  FROM Hotel.Reservation
  WHERE $1 = numero
  AND $2 < date_fin
  AND $3 > date_debut)
$$ LANGUAGE SQL;
