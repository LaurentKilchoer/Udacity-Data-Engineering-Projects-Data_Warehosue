import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop tables.
    Gets the list of drop table queries from the sql_queries script
    and runs them in the database using the cursor,
    commits the queries using the connection object.
    Parameters
    ----------
    cur : cursor object
    conn : database connection
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates tables.
    Gets the list of create table queries from the sql_queries script
    and runs them in the database using the cursor,
    commits the queries using the connection object.
    Parameters
    ----------
    cur : cursor object
    conn : database connection
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Main function of the create_tables script.
    Reads configuration file, 
    connects to database, 
    creates cursor object,
    Drops tables and creates tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()