-- reference
https://medium.com/@paramsingh96/optimizing-pattern-searching-queries-in-postgresql-84087d9bac8c

-- extension
create extension pg_trgm with schema pg_catalog;

-- create index
CREATE INDEX CONCURRENTLY trgm_index_pred_cpt ON myschema.prediction USING gin (lower(batch_source) gin_trgm_ops);

-- analyze query with index (100x faster)
explain analyze select * from myschema.prediction 
where lower(batch_source) like '%gpu%';
