import psycopg2
from psycopg2 import sql

# Database connection details
db_config = {
    'dbname': 'flipkart',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

# Connect to PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Create schema and table if not exists
def create_schema_and_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE SCHEMA IF NOT EXISTS flipkart_schema;
            CREATE TABLE IF NOT EXISTS flipkart_schema.flipkartdata (
                id SERIAL PRIMARY KEY,
                image_name VARCHAR(255),
                title VARCHAR(255),
                price NUMERIC
            );
        """)
        conn.commit()
        cur.close()
    except Exception as e:
        conn.rollback()
        print(f"Error creating schema or table: {e}")

# Insert data into the table
def insert_data(conn, data):
    try:
        cur = conn.cursor()
        insert_query = sql.SQL("""
            INSERT INTO flipkart_schema.flipkartdata (image_name, title, price)
            VALUES (%s, %s, %s);
        """)
        cur.executemany(insert_query, data)
        conn.commit()
        cur.close()
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")

def laptopdb(lp):
    # Example data to be inserted
    data_to_insert = [
        (lp['image_url'], lp['title'], lp['price']),
    ]
    
    # Connect to the database
    conn = connect_to_db()
    if conn is not None:
        # Create schema and table
        create_schema_and_table(conn)
        
        # Insert data
        insert_data(conn, data_to_insert)
        
        # Close the connection
        conn.close()

# if __name__ == "__main__":
#     main()