import os
import psycopg2  # pyright: ignore[reportMissingModuleSource]
import flask  # pyright: ignore[reportMissingImports]
from prometheus_flask_exporter import PrometheusMetrics  # pyright: ignore[reportMissingImports]

app = flask.Flask(__name__)

# Tích hợp Prometheus Metrics sẵn cho Bước 4
metrics = PrometheusMetrics(app)

# Lấy thông tin kết nối Database từ biến môi trường
DB_HOST = os.environ.get('DB_HOST', 'postgres_db')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'contract_management')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'StrongPassword123!')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS contracts (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                partner VARCHAR(200) NOT NULL,
                status VARCHAR(50) DEFAULT 'Draft',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing DB: {e}")

@app.route('/')
def index():
    return flask.jsonify({
        "message": "He thong Quan ly Hop dong (Contract Management System)",
        "status": "Running",
        "student_id": "DTC245160018"
    })

@app.route('/contracts', methods=['GET'])
def get_contracts():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, partner, status, created_at FROM contracts ORDER BY id DESC;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        contracts = []
        for r in rows:
            contracts.append({
                "id": r[0],
                "title": r[1],
                "partner": r[2],
                "status": r[3],
                "created_at": str(r[4])
            })
        return flask.jsonify({"success": True, "data": contracts})
    except Exception as e:
        return flask.jsonify({"success": False, "error": str(e)}), 500

@app.route('/contracts', methods=['POST'])
def create_contract():
    try:
        data = flask.request.get_json()
        title = data.get('title')
        partner = data.get('partner')
        status = data.get('status', 'Pending')

        if not title or not partner:
            return flask.jsonify({"success": False, "message": "Missing title or partner"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contracts (title, partner, status) VALUES (%s, %s, %s) RETURNING id;",
            (title, partner, status)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return flask.jsonify({"success": True, "message": "Contract created", "id": new_id}), 201
    except Exception as e:
        return flask.jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000)