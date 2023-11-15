-- First create extension if not exists
CREATE EXTENSION pg_stat_statements;

-- SELECT all and JOIN to get usernames
select pguser.usename, pgstat.*   
from pg_stat_statements as pgstat
left join pg_catalog.pg_user as pguser
	on pguser.usesysid = pgstat.userid ;
