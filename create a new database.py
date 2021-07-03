import sqlite3
## e
from mysql.connector import cursor

with sqlite3.connect("books.db") as db:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books(book_ID INTEGER  PRIMARY  KEY ,book_title VARCHAR (40)NOT NULL ,
    author VARCHAR (30) NOT NULL, price DECIMAL(10,5) NOT NULL , loan TRUE NOT NULL )
    ''')
cursor.execute("""
INSERT INTO books(book_title,author,price,loan)
VALUES ("Journey to the west","Wu Cheng'en",915.99,TRUE )
""")
db.commit()
cursor.execute("SELECT * FROM books")
print(cursor.fetchall())
