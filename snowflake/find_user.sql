-- Check if a user is registered in Snowflake
SELECT *
FROM snowflake.account_usage.users
WHERE name ilike '%<username>%'
    or login_name ilike '%<username>%'
