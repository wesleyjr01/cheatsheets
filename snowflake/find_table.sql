select 
    table_catalog database,
    table_schema schema,
    table_name
from snowflake.account_usage.tables
where table_type = 'BASE TABLE'
and table_name = <TABLE_NAME>
;
