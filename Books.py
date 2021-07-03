import sqlite3
###tt

class BooksDatabase:

    def books(self):
        books()


def books():
    book_title = input("Please enter the book you search for").title()
    with  sqlite3.connect("books.db") as db:
        cursor = db.cursor()
        find_user = "SELECT * FROM books WHERE  book_title = ? "
        cursor.execute(find_user, [book_title])
        result = cursor.fetchall()
        if result:
            for i in result:
                print("The book " + i[1], " is in the database")
                break

        else:
            print("Book not recognized in database")
            again = input("Do you want to try again (y/n):")
            if again.lower() == "n":
                print("Goodbye")
                return "exit"
            if again.lower() == "y":
                books()