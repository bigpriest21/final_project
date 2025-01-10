from app import app
from flask import render_template, request, jsonify, session, redirect, url_for
import sqlite3


# Secret key needed for sessions
app.secret_key = '09053361954' 


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = '5101520'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid credentials! Please try again."

    return render_template('login.html')


@app.route('/dashboard')
def admin_dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template("admin_dashboard.html")


@app.route('/admin/delete-booking/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM bookings WHERE id = ?', (booking_id,))
    conn.commit()

     # Reset the auto-increment to the correct value
    cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="bookings"')
    conn.commit()


    conn.close()
    return jsonify({'message': f'Booking with ID {booking_id} has been deleted.'})


@app.route('/admin/clear-bookings', methods=['DELETE'])
def clear_bookings():
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM bookings')
    conn.commit()

    # Reset the auto-increment to the correct value
    cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="bookings"')
    conn.commit()

    conn.close()
    return jsonify({'message': 'All bookings have been cleared.'})


@app.route('/bookings-data')
def bookings_data():
    # Optional: Protect this route too
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bookings')
    bookings = cursor.fetchall()
    conn.close()
    return jsonify(bookings)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

