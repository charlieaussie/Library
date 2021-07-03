import Books as Books

import time
import sys
import operator
import sqlite3
import os

#
db_books = Books


class Books:

    def __init__(self, title, author, price, loan, discount):
        self.title = title
        self.author = author
        self.price = price
        self.loan = loan
        self.discount = discount


def author_list(current_book):
    author_dictionaries = {hobbit.title: hobbit.author, lord_rings.title: lord_rings.author,
                           journey_to_west.title: journey_to_west.author}
    print("")
    temp = []
    author_dic = author_dictionaries
    res = dict()
    res_book = {key: author_dic[key] for key in author_dic.keys()
                & {lord_rings.title, lord_rings.author}}
    # printing result
    print(res_book, "Authors:" + str(author_dic))
    menu(current_book)


journey_to_west = Books(title="Journey to the west", author="Wu Cheng'en", price=850.50, loan=True,
                        discount=False)
hobbit = Books(title="Hobbit", author="J.R.R Tolkien", price=525.99, loan=True, discount=True)
lord_rings = Books(title="Lord of the rings", author="J.R.R Tolkien", price=625.99, loan=True,
                   discount=False)


def exit_program():
    sys.exit()


def loan_book_price_order(current_book):
    print("Books and prices")
    my_dict = {lord_rings.title: lord_rings.price, journey_to_west.title: journey_to_west.price,
               hobbit.title: hobbit.price}
    sorted_price = sorted(my_dict.items(), key=operator.itemgetter(1))
    print("Price in ascending order", sorted_price)
    author_list(current_book)


def check_discount(current_book):
    print("Special discount for some books")
    if current_book.discount == True:
        print(current_book.title, "has a special discount of 25%")
        discount = current_book.price * 0.25
        current_book.price -= discount
        discount_price = True
        time.sleep(1)
        print("Current price is now of", current_book.price)
        loan_book_price_order(current_book)
    else:
        print("Your book has no discount")
        discount_price = False
        loan_book_price_order(current_book)


def loan_book(current_book):
    current_book.loan = False
    choice = input("Are you sure you want to loan (y/n)")
    f = open("bookfile2.txt", "a")
    f.write(current_book.title)
    f.close()
    if choice.lower() == "y":
        print("You have successfully loaned ", current_book.title)
        check_discount(current_book)
    elif choice.lower() == "n":
        loan_status()
    else:
        print("Invalid input try again")
        loan_book(current_book)


def book_info(current_book):
    print("Book ", current_book.title, " Author is ", current_book.author, " Price is",
          current_book.price,
          "Loan is ", current_book.loan)
    if current_book.loan == False:
        print("That book is unavailable")
    elif current_book.loan:

        loan_book(current_book)


def loan_status():
    # db_books.books()
    loan = input("please enter the name of the book you want to loan ")
    if loan == lord_rings.title:
        current_book = lord_rings
        book_info(current_book)
    elif loan.lower().title() == hobbit.title:
        current_book = hobbit
        book_info(current_book)
    elif loan == journey_to_west.title:
        current_book = journey_to_west
        book_info(current_book)
    else:
        print("That book is unavailable")
        return loan_status()


def return_books(current_book):
    return_book = input("Do you want to return your book? (y/n)").lower()
    while return_book != "n":
        if return_book == "y":
            print("You have returned the book", current_book.title)
            current_book.loan = True
            os.remove("bookfile2.txt")

            menu(current_book)

        elif return_book == "n":
            menu(current_book)
        else:
            print("Wrong input try again")


def open_saved_file_books(current_book):
    if current_book.loan == False:
        f = open("bookfile2.txt")
        print("Loaned Book:", f.read())
        f.close()
        menu(current_book)
    elif current_book.loan:
        print("You have no books you are loaned for")
        time.sleep(1)
        menu(current_book)


# menu
def menu(current_book):
    global loan_status
    choice = 0
    choice = input(
        "What do you want to do?\n1 Loan Status\n2 Check discount\n3 Price order\n0 Exit\n4 File Book\n5 Return Book")
    while choice != "0":
        if choice == "0":
            exit_program()
        elif choice == "1":
            loan_status()
        elif choice == "2":
            check_discount(current_book)
        elif choice == "3":
            loan_book_price_order(current_book)
        elif choice == "4":
            open_saved_file_books(current_book)

        elif choice == "5":
            return_books(current_book)
        else:
            print("Invalid command try again")
            return menu(current_book)


##################
# loan_status()
##################

class Person:
    def __init__(self, email, pin_code, money):
        self.email = email
        self.pin_code = pin_code
        self.money = money


def login():
    for i in range(3):
        username = input("Please enter your username")
        password = input("Please enter your password")
        with  sqlite3.connect("create_account.db") as db:
            cursor = db.cursor()
            find_user = "SELECT * FROM account WHERE  username = ? AND password = ?"
            cursor.execute(find_user, [(username), (password)])
            result = cursor.fetchall()

            if result:
                for i in result:
                    print("Welcome " + i[3])
                    pin_code_and_email_info()
                else:
                    print("Username and Password not recognized")
                    again = input("Do you want to try again (y/n):")
                    if again.lower() == "n":
                        print("Goodbye")
                        time.sleep(1)
                        return ("exit")


def pin_code_and_email_info():
    for i in range(3):
        personal_pin_code = input("Please enter your pin code")
        email = input("Please enter your email")
        with  sqlite3.connect("create_account.db") as db:
            cursor = db.cursor()
            find_user = "SELECT * FROM account WHERE  personal_pin_code = ? AND email = ?"
            cursor.execute(find_user, [(personal_pin_code), (email)])
            result = cursor.fetchall()
            if result:
                for i in result:
                    print("Welcome " + i[3])
                    return loan_status()

                else:
                    print("pin code and email not recognized")
                    again = input("Do you want to try again (y/n):")
                    if again.lower() == "n":
                        print("Goodbye")
                        time.sleep(1)
                        return ("exit")


login()
