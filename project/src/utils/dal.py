import mysql.connector


class DAL:
    def __init__(self):
   
        self.connection = mysql.connector.connect(host="localhost",
                                                     user="root",
                                                     password="dc14785236",
                                                     database="travel_db"
                                                     )
        

    def get_table(self, sql):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql)
            table = cursor.fetchall()
            return table
        
    def get_one(self,sql, val=None):
        with self.connection.cursor(dictionary = True) as cursor:
            cursor.execute(sql,val)
            one = cursor.fetchone()
            return one
        
    def insert_dal(self, sql, val=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql,val)
            self.connection.commit()
            last_row = cursor.lastrowid
            return last_row
        
    def update_dal(self, sql, val=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql,val)
            self.connection.commit()
            row_id = cursor.rowcount
            return row_id
        
    def delete_dal(self, sql, val=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, val)
            self.connection.commit()
            row_id = cursor.rowcount
            return row_id



    def close(self):
        self.connection.close()
