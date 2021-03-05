--Jennifer Nguyen
--CPSC 408 Rene German
--Assignment 2

--1 create Player table
CREATE TABLE Player (
  pID       INT NOT NULL,
  name      VARCHAR(60) NOT NULL,
  teamName  VARCHAR(60),
  PRIMARY KEY (pID)
);

--2 alter Player table to add column, age
ALTER TABLE Player
ADD age INT;

--3 add values
INSERT INTO Player
VALUES (1, 'Player 1', 'Team A', 23),
       (2, 'Player 2', 'Team A', NULL),
       (3, 'Player 3', 'Team B', 28),
       (4, 'Player 4', 'Team B', NULL);

--4 delete Player 2
DELETE FROM Player
WHERE pID = 2;

--5 set age to 25 for NULL values
UPDATE Player
SET age = 25
WHERE age IS NULL;

--6 return num of tuples and average age
SELECT count(pID) tuple_count, avg(age) avg_age
FROM Player;

--7 drop PLayer table
DROP TABLE Player;

--8 return avg Total of invoices where country is Brazil
SELECT avg(Total) avg_total
FROM Invoice
WHERE BillingCountry = 'Brazil';

--9 like #8 but avg per billing city
SELECT BillingCity,avg(Total) avg_total
FROM Invoice
WHERE BillingCountry = 'Brazil'
GROUP BY BillingCity;

--10 return names of albums with 20+ tracks
SELECT A.Title, count(TrackID) num_tracks
FROM Album A
JOIN Track T on A.AlbumId = T.AlbumId
GROUP BY A.AlbumId HAVING count(TrackID) > 20;

--11 return num of invoices processed in 2010
SELECT count(*)
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2010';

--12 how many distinct billing cities are there in each billing country?
SELECT DISTINCT BillingCountry,count(BillingCity) distinct_cities
FROM Invoice
GROUP BY BillingCountry;

--13 album title, track title, media type for each record
SELECT A.Title album_title, T.Name track_title, M.Name media_type
FROM Album A
JOIN Track T on A.AlbumId = T.AlbumId
JOIN MediaType M on M.MediaTypeId = T.MediaTypeId;

--14 how many sales (invoice count) did Jane Peacock make as sales rep?
SELECT count(*) total_sales
FROM Invoice
JOIN Customer C on C.CustomerId = Invoice.CustomerId
JOIN Employee E on E.EmployeeId = C.SupportRepId
WHERE E.FirstName = 'Jane' AND E.LastName = 'Peacock';

--BONUS std dev of sum of totals in Invoice per billing country
SELECT sqrt(SUM(difference*difference)/count_country) mystddev
FROM
     (
         --get difference between country data and mean
         SELECT (SUM(Total) - avg_total) difference, count_country
         FROM Invoice,
              (
                  --get average of sum of totals, get number of countries
                  SELECT SUM(Total)/count(DISTINCT Invoice.BillingCountry) avg_total, count(DISTINCT Invoice.BillingCountry) count_country
                  FROM Invoice
                  )
         GROUP BY BillingCountry
         )
;

--check for extra credit
SELECT stdev(sum_total)
FROM (SELECT SUM(Total) sum_total
    FROM Invoice
    GROUP BY BillingCountry);

