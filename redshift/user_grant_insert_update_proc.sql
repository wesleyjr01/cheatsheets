CREATE OR REPLACE PROCEDURE public.grant_insert_update_access_to_user(username VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Grant usage on all schemas
    DECLARE
        schema_record RECORD;
    BEGIN
        FOR schema_record IN SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'padb_harvest')
        LOOP
            EXECUTE 'GRANT USAGE ON SCHEMA ' || quote_ident(schema_record.schema_name) || ' TO ' || quote_ident(username) || ';';
            EXECUTE 'GRANT SELECT ON ALL TABLES IN SCHEMA ' || quote_ident(schema_record.schema_name) || ' TO ' || quote_ident(username) || ';';
            EXECUTE 'GRANT INSERT ON ALL TABLES IN SCHEMA ' || quote_ident(schema_record.schema_name) || ' TO ' || quote_ident(username) || ';';
            EXECUTE 'GRANT UPDATE ON ALL TABLES IN SCHEMA ' || quote_ident(schema_record.schema_name) || ' TO ' || quote_ident(username) || ';';
            EXECUTE 'ALTER DEFAULT PRIVILEGES IN SCHEMA ' || quote_ident(schema_record.schema_name) || ' GRANT SELECT ON TABLES TO ' || quote_ident(username) || ';';
        END LOOP;
    END;
END;
$$;
