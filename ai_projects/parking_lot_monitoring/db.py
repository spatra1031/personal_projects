import psycopg2

# Database connection parameters
DB_NAME = "test_db"
DB_USER = "postgres"
DB_PASSWORD = "pass@6454439"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port

def create_database():
    """Creates a new database if it doesn't exist."""
    try:
        conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
        exists = cur.fetchone()
        
        if not exists:
            cur.execute(f"CREATE DATABASE {DB_NAME};")
            print(f"✅ Database '{DB_NAME}' created successfully!")
        else:
            print(f"ℹ️ Database '{DB_NAME}' already exists.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error creating database: {e}")

def create_table():
    """Creates a table in the database."""
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT,
                department VARCHAR(50)
            );
        """)
        conn.commit()
        print("✅ Table 'employees' created successfully!")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error creating table: {e}")

def insert_data():
    """Inserts sample data into the table."""
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cur = conn.cursor()
        
        employees = [
            ('Alice', 30, 'HR'),
            ('Bob', 25, 'Engineering'),
            ('Charlie', 35, 'Marketing')
        ]
        
        cur.executemany("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s);", employees)
        conn.commit()
        print("✅ Data inserted successfully!")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error inserting data: {e}")

def fetch_data():
    """Fetches and displays data from the table."""
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cur = conn.cursor()

        # Print the connected database name
        cur.execute("SELECT current_database();")
        db_name = cur.fetchone()[0]
        print(f"📌 Connected to database: {db_name}")

        cur.execute("SELECT * FROM employees;")
        rows = cur.fetchall()

        print("\n📌 Employee Records:")
        for row in rows:
            print(row)

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    create_database()
    create_table()
    insert_data()
    fetch_data()
