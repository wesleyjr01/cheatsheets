-- check where is located a particular column

select table_schema, table_name, column_name  FROM information_schema.columns
where table_name = 'batches'
and column_name = 'status';
