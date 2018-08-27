import psycopg2


def connect_to_db():
    # CREATE DATABASE supermarket
    # \connect supermarket
    # \dt - list tables
    queries = []

    queries.append("""
            CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY, 
                    user_role VARCHAR(255) NOT NULL, 
                    login_timestamp VARCHAR(255) NOT NULL 
            )
        """)

    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="supermarket", user="postgres", password="postgres")
        cur = conn.cursor()

        for query in queries:
            cur.execute(query)

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
