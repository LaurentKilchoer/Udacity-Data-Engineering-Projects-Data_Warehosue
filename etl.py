import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load staging tables.
    Loads values from S3 buckets into database.
    Parameters
    ----------
    cur : cursor object
    conn : database connection
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Insert values into tables.
    Gets the list of insert table queries from the sql_queries script
    and runs them in the database using the cursor,
    commits the queries using the connection object.
    Parameters
    ----------
    cur : cursor object
    conn : database connection
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Main function of the ETL script.
    Reads configuration file, 
    connects to database, 
    creates cursor object,
    load the stages tables,
    Insert data into final tables 
    and close the connection.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()