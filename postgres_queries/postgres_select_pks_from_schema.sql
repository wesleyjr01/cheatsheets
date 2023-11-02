with cte_ as (
	SELECT conrelid::regclass AS table_name,
	       conname AS primary_key,
	       pg_get_constraintdef(oid)
	FROM pg_constraint 
	WHERE contype = 'p' 
	AND connamespace = 'product'::regnamespace
	ORDER BY conrelid::regclass
)
select table_name, pg_get_constraintdef as PK from cte_;
