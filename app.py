import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Core Database Link Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'         
app.config['MYSQL_PASSWORD'] = '@BROTHERs#2025'  # Assign your explicit MySQL server root password here
app.config['MYSQL_DB'] = 'library__db'     
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# --- VISUAL WEB PANEL CONTROLLERS ---
@app.route('/')
@app.route('/index')
def index_page(): return render_template('index.html')

@app.route('/members')
def members_page(): return render_template('members.html')

@app.route('/books')
def books_page(): return render_template('books.html')

@app.route('/borrow')
def borrow_page(): return render_template('borrow.html')

@app.route('/fines')
def fines_page(): return render_template('fines.html')

@app.route('/publisher') # Serving Staff profiles via publisher routing configuration
def publisher_page(): return render_template('publisher.html')


# --- CENTRALIZED OPERATIONAL CRUD UTILITY CONTROLLER ---
def execute_database_crud(table_name, primary_key, columns):
    cur = mysql.connection.cursor()
    
    if request.method == 'GET':
        cur.execute(f"SELECT * FROM {table_name}")
        records = cur.fetchall()
        cur.close()
        return jsonify(records)
        
    elif request.method == 'POST':
        payload = request.json
        # Handle structural auto-increment exclusion for incoming IDs if requested
        active_columns = [col for col in columns if col in payload]
        cols_str = ", ".join(active_columns)
        placeholders = ", ".join(["%s"] * len(active_columns))
        values = [payload.get(c) for c in active_columns]
        
        cur.execute(f"INSERT INTO {table_name} ({cols_str}) VALUES ({placeholders})", values)
        mysql.connection.commit()
        cur.close()
        return jsonify({"success": True, "message": "Record inserted cleanly."})
        
    elif request.method == 'PUT':
        payload = request.json
        pk_val = payload.get(primary_key)
        update_cols = [c for c in columns if c != primary_key and c in payload]
        set_clause = ", ".join([f"{c} = %s" for c in update_cols])
        values = [payload.get(c) for c in update_cols] + [pk_val]
        
        cur.execute(f"UPDATE {table_name} SET {set_clause} WHERE {primary_key} = %s", values)
        mysql.connection.commit()
        cur.close()
        return jsonify({"success": True, "message": "Record modified cleanly."})
        
    elif request.method == 'DELETE':
        pk_val = request.args.get('id')
        cur.execute(f"DELETE FROM {table_name} WHERE {primary_key} = %s", [pk_val])
        mysql.connection.commit()
        cur.close()
        return jsonify({"success": True, "message": "Record eliminated cleanly."})

# --- LIVE REVOLVING BACKEND ENDPOINT DIRECTIVES ---
@app.route('/api/members', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_members():
    return execute_database_crud('Member', 'member_id', ['member_id', 'name', 'phone', 'membership_date'])

@app.route('/api/books', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_books():
    return execute_database_crud('Book', 'book_id', ['book_id', 'title', 'author_id', 'category', 'price', 'availability'])

@app.route('/api/borrowings', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_borrowings():
    return execute_database_crud('Issue', 'issue_id', ['issue_id', 'member_id', 'book_id', 'issue_date', 'return_date'])

@app.route('/api/fines', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_fines():
    return execute_database_crud('Fine', 'fine_id', ['fine_id', 'member_id', 'amount', 'paid_status'])

@app.route('/api/staff', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_staff():
    return execute_database_crud('Staff', 'staff_id', ['staff_id', 'name', 'role'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)