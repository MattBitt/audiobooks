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
        if len(self.get_book(table, record['id'])) > 0:
            self.delete_record(table, record['id'])
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
        
    def get_book(self, table, id):
        query = "SELECT * FROM {} WHERE id = '{}'".format(table, id)
        return self.run_query(query)
        
    def delete_record(self, table, id):
        query = "DELETE FROM {} WHERE id = '{}'".format(table, id)
        self.execute_query(query)
        
    def get_all_info_from_db(self):
        """ This function retrieves all of the data from the the table "books"
            returns:  List of dictionaries containing all of the audiobook info """
        
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        query = """SELECT * FROM books ORDER BY date_added DESC"""
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()