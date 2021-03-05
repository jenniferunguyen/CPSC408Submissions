--1 returns max billing total in invoice table
SELECT max(total) max_billing
FROM Invoice;

--2 return max billing total in invoice without aggregate
SELECT *
FROM Invoice
ORDER BY Total DESC LIMIT 1;

--3 find media type name with total num of tracks
SELECT m.Name, count(t.TrackId) num_of_tracks
FROM Track t
INNER JOIN MediaType m
ON m.MediaTypeId = t.MediaTypeId
GROUP BY m.Name;

--4 add to 3, order by num in desc
SELECT m.Name, count(t.TrackId) num_of_tracks
FROM Track t
INNER JOIN MediaType m
ON m.MediaTypeId = t.MediaTypeId
GROUP BY m.Name
ORDER BY num_of_tracks DESC;

--5 add to 4, only num > 200
SELECT m.Name, count(t.TrackId) num_of_tracks
FROM Track t
INNER JOIN MediaType m
ON m.MediaTypeId = t.MediaTypeId
GROUP BY m.Name HAVING(num_of_tracks > 200)
ORDER BY num_of_tracks DESC;

--6 find num of tracks for "A" artist names, and count of such artists
SELECT count(T.TrackId) num_of_tracks
FROM Track T
JOIN Album A on A.AlbumId = T.AlbumId
JOIN Artist A2 on A.ArtistId = A2.ArtistId
WHERE A2.Name LIKE "A%";

SELECT count(*) total_tracks, count(DISTINCT art.Name) artist_count
FROM Artist art
JOIN Album al on art.ArtistId = al.ArtistId
JOIN Track T on al.AlbumId = T.AlbumId
WHERE art.Name LIKE "A%"

--7 return first name, last name, birth date, birth decade of employees
SELECT FirstName||" "||LastName full_name, BirthDate,
       CASE WHEN BirthDate BETWEEN '1940-01-01' and '1950-01-01' THEN '40s'
            WHEN BirthDate BETWEEN '1950-01-01' and '1960-01-01' THEN '50s'
            WHEN BirthDate BETWEEN '1960-01-01' and '1970-01-01' THEN '60s'
        ELSE '70s'
        END Decade
FROM Employee

--SUB QUERIES
SELECT *
FROM Customer
WHERE Country IN
    (
        SELECT DISTINCT Country
        FROM Customer
        WHERE PostalCode = '70174'
        or Fax IS NOT NULL
    );

