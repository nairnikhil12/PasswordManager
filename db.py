import sqlite3

# take the record as a tuple and inserts it into the database
# (application_name, url, email_id, password)
def insert_record(record):
    con = sqlite3.connect('password_database.db')

    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS
    password(application_name text, url text, email_id text, password text)''')

    cur.execute("INSERT INTO password VALUES(?, ?, ?, ?)", record)

    con.commit()

    con.close()

# fetches and returns all the records from the database
# where the application name matches with the parameter given
def fetch_records(prefix):
    con = sqlite3.connect('password_database.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS
    password(application_name text, url text, email_id text, password text)''')

    cur.execute(f"SELECT * FROM password WHERE application_name LIKE \'{prefix}%\'")

    res = cur.fetchall()
    con.close()

    return res
