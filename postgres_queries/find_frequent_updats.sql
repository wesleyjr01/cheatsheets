-- tables with too many updates may need periodic re-index operations
with cte_ as (
	select 
		relname
		,n_tup_ins
		,n_tup_upd
		,n_tup_del
		,(case when (n_tup_ins + n_tup_upd + n_tup_del) = 0 then 1 else (n_tup_ins + n_tup_upd + n_tup_del) end) as sum_
	FROM pg_stat_user_tables 
)
SELECT relname,
       cast(n_tup_ins AS numeric) / sum_ AS ins_pct,
       cast(n_tup_upd AS numeric) / sum_ AS upd_pct,
       cast(n_tup_del AS numeric) / sum_ AS del_pct 
FROM cte_ 
       ORDER BY relname;
