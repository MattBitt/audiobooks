import sqlite3

tableName = "books"

def getBook(id):
    pass
    
def addBook(dbPath, info):
    conn = sqlite3.connect(dbPath)
    query = """INSERT INTO books (id, title, author, series, volume, year, dateAdded, length,
            url, fileSize, deleted, imagePath) VALUES 
            ('{id}', '{title}', '{author}', '{series}', '{volume}', {year}, 
            '{dateAdded}', {length}, '{url}', {fileSize}, {deleted}, '{imagePath}')""".format(**info)
      conn.execute(query)
    conn.commit()    

   