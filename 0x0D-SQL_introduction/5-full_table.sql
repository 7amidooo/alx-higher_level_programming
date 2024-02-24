-- describe the table 
select * 
FROM INFORMATION_SCHEMA.COLUMNS
where TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
