from crypt import methods
from turtle import title
#db 追加
from flaskr import app, db
from flask import render_template, request, redirect, url_for

from flaskr.db import DATABASE

import sqlite3
DATABASE = "database.db"


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute("SELECT * FROM books").fetchall()
    con.close


    books = []
    for row in db_books:

        
        books.append({"id": row[0], "title": row[1], "price": row[2], "arrival_day": row[3]})

    return render_template(
        'index.html',books=books
    )

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/register", methods=["POST"])
def register():
    title = request.form["title"]
    price = request.form["price"]
    arrival_day =request.form["arrival_day"]

    con = sqlite3.connect(DATABASE)

    
    con.execute('INSERT INTO books (title, price, arrival_day) VALUES(?, ?, ?)',[title, price, arrival_day])

    con.commit()
    con.close()
    return redirect(url_for("index"))




#sum_code1
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    con = sqlite3.connect(DATABASE)
    if request.method == 'POST':
        con.execute('DELETE FROM books WHERE id = ?', [id])
        con.commit()
        con.close()
        return redirect(url_for('index'))
    else:
        book = con.execute('SELECT * FROM books WHERE id = ?', [id]).fetchone()
        con.close()
        if book:
            return render_template('delete.html', book=book)
        else:
            return "Book not found", 404


