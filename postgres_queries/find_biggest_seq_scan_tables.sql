SELECT schemaname, relname,seq_scan, idx_scan,
       cast(idx_scan AS numeric) / (idx_scan + seq_scan)
       AS idx_scan_pct 
FROM pg_stat_user_tables 
       WHERE (idx_scan + seq_scan) > 0 ORDER BY idx_scan_pct;
