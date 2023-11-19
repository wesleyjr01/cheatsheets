-- find how often an index has been used and it's size
SELECT schemaname, relname, indexrelname, idx_scan,
       pg_size_pretty(pg_relation_size(indexrelid)) AS idx_size
FROM   
	   pg_stat_user_indexes;
