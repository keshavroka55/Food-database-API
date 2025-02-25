from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    'host': 'sql205.infinityfree.com',  # MySQL Hostname
    'user': 'if0_38392260',             # MySQL Username
    'password': 'eOYV27NhPEf',          # MySQL Password (Never share in production)
    'database': 'if0_38392260_nepalifood'  # Your Database Name
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        return str(err)

@app.route('/')
def home():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database Connection Failed: {conn}"
    
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return f"Connected! Tables: {tables}"

if __name__ == '__main__':
    app.run(debug=True)
