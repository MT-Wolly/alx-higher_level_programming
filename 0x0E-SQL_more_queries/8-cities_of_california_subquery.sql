-- lists all the cities of California registered in the database
-- query to list all ther cities from california
SELECT id, name 
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California");
