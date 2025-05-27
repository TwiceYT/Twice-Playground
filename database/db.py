import sqlite3

# Function to set up the database connection and create tables
def setup():
    try:
        # Connect to the database
        db_connection = sqlite3.connect('TwiceFun.db')
        cursor = db_connection.cursor()


        #MessageStats Database
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS msgstats (
            guild_id INTEGER,
            user_id INTEGER,
            user TEXT,
            msg INTEGER,
            last_message_timestamp DATETIME
        )
        """)

        #Birthdays
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS birthdays (
            guild_id INTEGER,
            user_id INTEGER,
            user TEXT,
            birthdate INTEGER
        )
        """);
        # Commit changes and return connection and cursor
        db_connection.commit()
        return db_connection, cursor

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None, None
    except Exception as e:
        print("Error during database setup:", e)
        return None, None