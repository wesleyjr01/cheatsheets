-- select id, count(*) from db.table group by 1 having count(*) > 1;


-- WITH name_of_cte AS (
-- SELECT *, extract(month from reportstartdate) as month, extract(year from reportstartdate) as year
-- FROM "db"."table"
-- ) 
-- select * from name_of_cte


-- CREATE TABLE IF NOT EXISTS default.test_wesley_db
-- WITH (
--     format = 'Parquet'
--     ,parquet_compression='SNAPPY'
--     ,external_location = 's3://bucketname/test_wesley_db/'
-- ) AS
-- SELECT * FROM db.table2
-- ;


-- dedup query
-- SELECT count(*), id FROM "raw-db-develop-us-east-1"."auditlog"  group by id having count(*)>1;
