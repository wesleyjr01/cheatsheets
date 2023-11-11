-- check for bloat
select schemaname, relname, n_live_tup, n_dead_tup  from pg_catalog.pg_stat_user_tables;
