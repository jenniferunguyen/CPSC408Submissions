--1
SELECT FirstName, LastName, Email
FROM Employee;

--2
SELECT *
FROM Artist;

--3
SELECT *
FROM Employee
WHERE Title LIKE '%Manager';

--4
SELECT InvoiceId, max(Total)
FROM Invoice;
SELECT InvoiceId, min(Total)
FROM Invoice;

--5
SELECT BillingAddress,BillingCity,BillingPostalCode,Total
FROM Invoice
WHERE BillingCountry = 'Germany';

--6
SELECT BillingAddress,BillingCity,BillingPostalCode,Total
FROM Invoice
WHERE Total > 15 AND Total < 25;

--7
SELECT DISTINCT BillingCountry
FROM Invoice;

--8
SELECT FirstName, LastName,CustomerId,Country
FROM Customer
WHERE Country <> 'USA';

--9
SELECT FirstName, LastName,CustomerId,Country
FROM Customer
WHERE Country = 'Brazil';

--10
SELECT InvoiceId,Name
FROM InvoiceLine
INNER JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
ORDER BY Track.Name;