import sqlite3
import os

class MYDB(object):
    def __init__(self, db_path):
        if os.path.exists(db_path):
            self.db = db_path
        
        else:
            raise Exception("File {} not found".format(db_path))
            
    def run_query(self, query):
        conn = sqlite3.connect(self.db)    
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
        
    def execute_query(self, query):
        conn = sqlite3.connect(self.db)    
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        
        
    def select_all(self, table):
        conn = sqlite3.connect(self.db)    
        query = """SELECT * FROM {} """.format(table)
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
        
    def insert_record(self, table, record):
        query = """INSERT INTO {} (id, title, author, series, volume, year, date_added, duration, \
            local_url, file_size, deleted, local_image_url, description) VALUES """.format(table)
        query += """('{id}', '{title}', '{author}', '{series}', '{volume}', {year}, \
            '{date_added}', {duration}, '{local_url}', {file_size}, {deleted}, '{local_image_url}', '{description}')""".format(**record)
        self.execute_query(query)
    def count_records(self, table):
        return self.run_query("SELECT COUNT() from {}".format(table))[0][0]
        
    def delete_all(self, table):
        query = "DELETE FROM {}".format(table)
        self.execute_query(query)