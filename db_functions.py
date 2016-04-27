import sqlite3

def getBook(id):
    pass
    
def add_book_to_db(db_path, info):
    """ This function writes an audiobook to the database table books.
        db_path = String containing the full path to the database
        info = Dictionary containing all of the infomation about the audiobook.
               This dictionary must have each field listed below 
        returns:  Nothing"""
        
    conn = sqlite3.connect(db_path)
    query = """INSERT INTO books (id, title, author, series, volume, year, date_added, duration, \
            url, file_size, deleted, image_url, description) VALUES \
            ('{id}', '{title}', '{author}', '{series}', '{volume}', {year}, \
            '{date_added}', {duration}, '{url}', {file_size}, {deleted}, '{image_url}', '{description}')""".format(**info)
    conn.execute(query)
    conn.commit()   
    conn.close()

def get_all_info_from_db(db_path):
    """ This function retrieves all of the data from the the table "books"
        db_path = String containing the full path to the database
        returns:  List of dictionaries containing all of the audiobook info """
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    query = """SELECT * FROM books ORDER BY date_added DESC"""
    cursor = conn.cursor()
    cursor.execute(query)
    infos = []
    return cursor.fetchall()


if __name__ == "__main__":
    get_all_info_from_db('audiobooks.db')
        