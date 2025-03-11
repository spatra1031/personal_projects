import psycopg2

# PostgreSQL Database Connection Parameters
DB_PARAMS = {
    "dbname": "parking_db",
    "user": "postgres",
    "password": "pass@6454439",
    "host": "localhost",  # Change if remote
    "port": "5432"
}

def connect_to_db(config):
    try:
        conn = psycopg2.connect(**config)
        return conn
    except psycopg2.Error as e:
        print(f"Failed to connect to database: {e}")
        return None

def upload_data_to_db(conn, data):
    try:
        cur = conn.cursor()
        sql = """
            INSERT INTO parking_status (id, status)
            VALUES (%s, %s)
            ON CONFLICT (id) DO UPDATE SET status = EXCLUDED.status;
        """
        for spot_id, status in data:
            cur.execute(sql, (spot_id, status))
        conn.commit()
        cur.close()
        print("Data uploaded successfully!")
    except psycopg2.Error as e:
        print(f"Error uploading data: {e}")

# Example data to upload
data_to_upload = [
    ("A1", "occupied"),
    ("A2", "empty"),
    ("B1", "occupied")
]

# Establish a connection
conn = connect_to_db(DB_PARAMS)

if conn:
    # Upload data
    upload_data_to_db(conn, data_to_upload)
    # Close the connection
    conn.close()
else:
    print("Failed to connect to database.")
