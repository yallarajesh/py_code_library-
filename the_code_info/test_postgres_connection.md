# test_postgres_connection

Reads a Postgres connection URL from an environment variable and tests connecting to it with psycopg2, reporting server version and connection details.

## functions exposed
- get_database_url(env_var_name="DATABASE_URL") -> the connection URL string, raises ValueError if the environment variable is not set
- test_postgres_connection(env_var_name="DATABASE_URL") -> dict with status, and either version/host/port/dbname/user on success or error on failure

## dependencies
psycopg2-binary

## env vars required
DATABASE_URL (or a custom name passed as env_var_name), format: postgresql://user:password@host:port/dbname

## tags
postgres, psycopg2, database, connection test, sql

## status
tested, passing (missing env var, unreachable host, and live successful connection all verified)

## path
task_test_postgres_connection/test_postgres_connection.py
