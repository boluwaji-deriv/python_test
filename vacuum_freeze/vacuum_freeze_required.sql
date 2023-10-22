SELECT
  age(relfrozenxid)::NUMERIC / current_setting('autovacuum_freeze_max_age')::NUMERIC AS measure,
  t1.oid::regclass::text AS table_name,
  t2.rolname AS table_owner,
  pg_size_pretty(pg_relation_size(t1.oid)) AS tablesize, 
  CASE
    WHEN t1.relkind = 'r' THEN 'ordinary table'
    WHEN t1.relkind = 'i' THEN 'index'
    WHEN t1.relkind = 'S' THEN 'sequence'
    WHEN t1.relkind = 't' THEN 'TOAST table'
    WHEN t1.relkind = 'v' THEN 'view'
    WHEN t1.relkind = 'm' THEN 'materialized view'
    WHEN t1.relkind = 'c' THEN 'composite type'
    WHEN t1.relkind = 'f' THEN 'foreign table'
    WHEN t1.relkind = 'p' THEN 'partitioned table'
    WHEN t1.relkind = 'I' THEN 'partitioned index'
    ELSE 'unknown'
  END AS relkind_description
 FROM pg_class t1
 LEFT JOIN pg_authid t2 ON t1.relowner = t2.oid
WHERE pg_relation_size(t1.oid)>=2::bigint*1024  
  AND relkind IN ('r', 't')
ORDER BY 1 DESC  
LIMIT 10;



