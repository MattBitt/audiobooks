import sqlite3


def create_books_table()
    conn = sqlite3.connect("audiobooks.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE books
             (id text, title text, author text, series text, volume integer,
             year integer, date_added text, duration real, url text, size real,
             deleted integer, image_path text)''')
    conn.commit()
    conn.close()

def
