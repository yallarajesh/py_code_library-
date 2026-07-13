"""
test_postgres_connection

Reads a Postgres connection URL from an environment variable, attempts
a connection with psycopg2, and returns a dict describing the result.
No arguments carry credentials directly, the URL always comes from the
environment.
"""

import os
import psycopg2


def get_database_url(env_var_name="DATABASE_URL"):
    """
    Read the Postgres connection URL from an environment variable.

    env_var_name: name of the environment variable holding the URL

    Returns the URL as a string.

    Raises ValueError if the environment variable is not set.
    """
    url = os.environ.get(env_var_name)

    if not url:
        raise ValueError(f"Environment variable '{env_var_name}' is not set")

    return url


def test_postgres_connection(env_var_name="DATABASE_URL"):
    """
    Attempt to connect to Postgres using a URL read from an
    environment variable, and report the result.

    env_var_name: name of the environment variable holding the connection URL

    Returns a dict with the following keys:
    status: "connected" or "failed"
    version: the Postgres server version string, present when connected
    host, port, dbname, user: connection details, present when connected
    error: the error message, present when failed
    """
    try:
        url = get_database_url(env_var_name)
    except ValueError as exc:
        return {"status": "failed", "error": str(exc)}

    conn = None
    try:
        conn = psycopg2.connect(url)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        cursor.close()

        params = conn.get_dsn_parameters()

        result = {
            "status": "connected",
            "version": version,
            "host": params.get("host"),
            "port": params.get("port"),
            "dbname": params.get("dbname"),
            "user": params.get("user"),
        }

    except Exception as exc:
        result = {"status": "failed", "error": str(exc)}

    finally:
        if conn is not None:
            conn.close()

    return result
