-- Format output to be more readable (putting this first so all queries are formatted)
.mode column
.headers on

-- Show all tables in the database
.tables

-- Show the schema of the person table
.schema person

-- Show all records in the person table
SELECT * FROM person;

-- Show the total number of records
SELECT COUNT(*) as total_records FROM person;

-- Show the average age
SELECT AVG(age) as average_age FROM person;

-- Show records grouped by city
SELECT city, COUNT(*) as count 
FROM person 
GROUP BY city;

-- Show the latest 5 records
SELECT * FROM person 
ORDER BY created_at DESC 
LIMIT 5;

-- Show all people older than 30
SELECT * FROM person 
WHERE age > 30;

-- Find people whose names start with 'B'
SELECT * FROM person 
WHERE name LIKE 'B%';

-- Sort everyone by age (oldest to youngest)
SELECT name, age, city 
FROM person 
ORDER BY age DESC;

-- Get detailed age statistics
SELECT 
    MIN(age) as youngest,
    MAX(age) as oldest,
    AVG(age) as average_age,
    COUNT(*) as total_people
FROM person;

-- Show cities with average age per city
SELECT 
    city,
    COUNT(*) as people_count,
    AVG(age) as average_age
FROM person 
GROUP BY city
ORDER BY people_count DESC;

-- Show records created today
SELECT * FROM person 
WHERE date(created_at) = date('now');

-- Show names in alphabetical order
SELECT name, age, city 
FROM person 
ORDER BY name ASC; 