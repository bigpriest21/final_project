from app import app
from flask import render_template, request, jsonify, redirect, url_for, flash
import sqlite3

@app.route('/bookingpage', methods=['GET'])
def bookingpage():
    return render_template("bookingpage.html")

#Form Submission
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    
    #Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    reason = request.form.get('reason')
    booking_time = request.form.get('booking_time')
    booking_date = request.form.get('booking_date')



    # Processes the data
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Reason: {reason}")
    print(f"Time: {booking_time}")
    print(f"Date: {booking_date}")

      # Save to database
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bookings (name, email, phone, reason, booking_time, booking_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, reason, booking_time, booking_date))
    conn.commit()
    conn.close()

    # Flash success message
    flash('Booking received successfully!', 'success')

     # Redirect to the booking page to display the message
    return redirect('/bookingpage')

@app.route('/view-bookings', methods=['GET'])
def view_bookings():
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bookings')
    bookings = cursor.fetchall()
    conn.close()

    return jsonify(bookings)
