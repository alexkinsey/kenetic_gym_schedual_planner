import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []

    try:
        urlparse.uses_netloc.append("postgres") 
        connection_params = urlparse.urlparse(os.environ["DATABASE_URL"])
        db_connection = psycopg2.connect(database = connection_params.path[1:], user = connection_params.username, password = connection_params.password, host = connection_params.hostname, port = connection_params.port)

        conn=psycopg2.connect("dbname='gym_core'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
