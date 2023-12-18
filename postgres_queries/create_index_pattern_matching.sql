-- extension
create extension pg_trgm with schema pg_catalog;

-- create index
CREATE INDEX CONCURRENTLY trgm_index_pred_cpt ON myschema.prediction USING gin (lower(batch_source) gin_trgm_ops);

-- analyze query with index (100x faster)
explain analyze select * from myschema.prediction 
where lower(batch_source) like '%gpu%';
