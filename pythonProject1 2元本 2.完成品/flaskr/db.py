import sqlite3

DATABASE = "database.db"

def create_books_table():
    con = sqlite3.connect(DATABASE)
    # books (title, price, arrival_day)")にidを追加
    # 修正前　con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)")
    #CERATE文のところで「id INTEGER PRIMARY KEY AUTOINCREMENT」を追加。
    #これは「id」と言う名前のカラムを作成id の型（整数）、主キー制約（PRIMARY KEY）、自動付番（AUTOINCREMENT）を設定の意味。
    # 2番目のように設定する理由はidの重複を防ぐため。仮にidの重複を許してしまうと、削除する時に書籍を区別できず、指定した書籍と別の書籍を削除してしまう可能性があり。
    con.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title, price, arrival_day)")
    con.close()
