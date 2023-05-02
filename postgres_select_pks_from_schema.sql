SELECT conrelid::regclass AS table_name,
       conname AS primary_key,
       pg_get_constraintdef(oid)
FROM pg_constraint 
WHERE contype = 'p' 
AND connamespace = 'rpt'::regnamespace
ORDER BY conrelid::regclass
;
