# Create a temporary file to store ALTER SYSTEM commands
temp_file=$(mktemp /tmp/pg_reset.XXXXXX)
srv=db_clusters
pg_port=5432  # Default port for PostgreSQL
# Generate ALTER SYSTEM commands and write them to the file
if psql service=$srv -p $pg_port -X -At -c "SELECT 'ALTER SYSTEM RESET ' || name || ';' FROM pg_settings WHERE sourcefile ~ '/postgresql.auto.conf' AND name NOT IN ('primary_conninfo', 'synchronous_standby_names')" > "$temp_file"; then
    echo "Generated ALTER SYSTEM commands successfully."
else
    echo "Error generating ALTER SYSTEM commands."
    exit 1
fi
# Execute the generated ALTER SYSTEM commands
psql service=$srv -p $pg_port -f "$temp_file"

# Reload the configuration
psql service=$srv -p $pg_port -c "SELECT pg_reload_conf();"

# Remove the temporary file
rm "$temp_file"

for i in test-{m,s}{a,b,c}x; do     echo ${i};     psql service=${i} -p 5432 -c "select name, setting from pg_settings where sourcefile ~ '/postgresql.auto.conf' AND name NOT IN ('primary_conninfo', 'synchronous_standby_names');";      done

SELECT name, setting 
  FROM pg_settings 
 WHERE name IN ('checkpoint_timeout', 'log_checkpoints', 'log_min_duration_statement', 'maintenance_work_mem', 'max_parallel_maintenance_workers', 'max_wal_size', 'max_worker_processes', 'wal_keep_size'); 
