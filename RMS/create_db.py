import sqlite3

def create_rms_db():
    try:
        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        # Create courses table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)
        con.commit()

        # Create student table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                roll INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                gender TEXT,
                dob TEXT,
                contact TEXT,
                admission TEXT,
                course TEXT,
                state TEXT,
                city TEXT,
                pin TEXT,
                address TEXT
            )
        """)
        con.commit()

        # Create result table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT,
                name TEXT,
                course TEXT,
                marks_ob TEXT,
                full_marks TEXT,
                per TEXT
            )
        """)
        con.commit()

        print("Database and tables created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    create_rms_db()
