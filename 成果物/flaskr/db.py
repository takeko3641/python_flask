import sqlite3

DATABASE = "database.db"

def create_books_table():
    con = sqlite3.connect(DATABASE)
    
    con.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title, price, arrival_day)")
    con.close()
