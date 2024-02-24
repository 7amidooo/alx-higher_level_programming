-- Show number of records 
SELECT COUNT(SELECT id FROM first_table WHERE ID = 89) FROM first_table;
