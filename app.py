from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(_name_)
DATABASE = 'expenses.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    conn = get_db()
    try:
        cursor = conn.execute('SELECT * FROM expenses')
        expenses = cursor.fetchall()
    except sqlite3.OperationalError:
        expenses = []
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    conn = get_db()
    conn.execute('INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)', 
                (request.form['description'], request.form['amount'], request.form['category']))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)