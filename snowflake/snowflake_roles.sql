-- Show metadata of a role
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.ROLES
where name ilike '%<role_name>%';

-- Check all users attached to a role
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_USERS
WHERE role = <role_name>;


-- Show all permission grants related to a role
SHOW GRANTS TO ROLE <role_name>;
