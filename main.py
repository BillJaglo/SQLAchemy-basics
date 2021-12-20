import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

## CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True)
    author = db.Column(db.String(250))
    rating = db.Column(db.Float)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


## ********* CRUD - Create Read Update Delete ********* ##

# CREATE RECORD
new_book = Book(title="Yo mama", author="testing", rating=10.0)
db.session.add(new_book)
db.session.commit()

## READ ALL RECORDS
# puts all records into a list as an object
all_books = db.session.query(Book).all()

## READ A PARTICULAR RECORD
# pulls out particular object in database
book = Book.query.filter_by(title="Harry Potter").first()

## UPDATE A PARTICULAR RECORD BY QUERY
# updates a particular object in database by pulling in from a query first
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

## UPDATE A PARTICULAR RECORD BY ID
# updates a particular object in database by ID/primary key
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

## DELETE A PARTICULAR RECORD BY PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()












# **********how to create and edit a database with sqlite3***********
# # create collection to the database.  If the database does not exist, then it will be created
# db = sqlite3.connect("books-collection.db")
#
# # create cursor to control database
# cursor = db.cursor()
#
# # # create a new table with the name of 'books'. the lowercase in the () are the fields in the table aka column headings
# # # primary key is one piece of data that will uniquely identify this record in the table
# # # eg of primary key is a human's passport.  The passport identifies the humand since no two passport IDs will be the same
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# # add a book to the database
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
# **********how to create and edit a database with sqlite3***********



