import sqlite3

# Function to create tables
def create_tables():
    # Connect to the database
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()

    # Create bookings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        reason TEXT,
        booking_time TEXT,
        booking_date TEXT
    )
    ''')

    # Create subscribers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Execute the function to create tables
if __name__ == '__main__':
    create_tables()
