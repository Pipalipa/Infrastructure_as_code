from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'db'),  
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/data')
def data():
    connection = None
    try:
        connection = get_db_connection()
        if connection is None:
            raise Exception("Failed to connect to the database")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        result = cursor.fetchall()
        # Convert the result to a list of dictionaries
        result_dict = [{'id': row[0], 'name': row[1], 'value': row[2]} for row in result]
        return jsonify(result_dict)
    except mysql.connector.Error as err:
        app.logger.error(f"MySQL error: {err}")
        return str(err), 500
    except Exception as e:
        app.logger.error(f"General error: {e}")
        return str(e), 500
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('/certs/server.crt', '/certs/server.key'))
