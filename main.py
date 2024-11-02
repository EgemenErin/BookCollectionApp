from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

def get_db_connection():
    connection = sqlite3.connect("books-collection.db")
    connection.row_factory = sqlite3.Row  # Enables dictionary-like access to rows
    return connection

with get_db_connection() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title VARCHAR(250) NOT NULL UNIQUE,
            author VARCHAR(250) NOT NULL,
            rating FLOAT NOT NULL
        )
    """)
    db.commit()

class AddBookForm(FlaskForm):
    bookname = StringField('Bookname', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditRatingForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Update Rating')


@app.route('/')
def home():
    with get_db_connection() as db:
        books = db.execute("SELECT * FROM books").fetchall()
    return render_template("index.html", books=books)


@app.route("/remove/<int:book_id>")
def remove(book_id):
    with get_db_connection() as db:
        db.execute("DELETE FROM books WHERE id = ?", (book_id,))
        db.commit()
    return redirect(url_for('home'))


@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    form = EditRatingForm()

    with get_db_connection() as db:
        book = db.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()

    if form.validate_on_submit():
        new_rating = form.rating.data
        with get_db_connection() as db:
            db.execute("UPDATE books SET rating = ? WHERE id = ?", (new_rating, book_id))
            db.commit()
        return redirect(url_for('home'))
    form.rating.data = book["rating"]
    return render_template("edit.html", form=form, book=book)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        new_book = {
            'bookname': form.bookname.data,
            'author': form.author.data,
            'rating': form.rating.data
        }
        with get_db_connection() as db:
            db.execute("INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
                       (new_book['bookname'], new_book['author'], new_book['rating']))
            db.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)

