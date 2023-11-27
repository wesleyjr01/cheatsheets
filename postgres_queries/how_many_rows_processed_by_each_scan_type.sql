SELECT relname, seq_tup_read, idx_tup_fetch,
       cast(idx_tup_fetch AS numeric) / (idx_tup_fetch + seq_tup_read) 
       AS idx_tup_pct 
FROM pg_stat_user_tables 
       WHERE (idx_tup_fetch + seq_tup_read) > 0 ORDER BY idx_tup_pct;
