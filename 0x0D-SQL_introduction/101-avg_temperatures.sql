-- Display data in file
SELECT city , AVG(value) AS                
avg_temp FROM temperatures 
ORDER BY value DESC;
