import sqlite3
from mysql.connector import cursor

with sqlite3.connect("create_account.db") as db:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS account(pin_code_ID INTEGER  PRIMARY  KEY ,personal_pin_code INTEGER NOT NULL ,
    email VARCHAR (30) NOT NULL, username VARCHAR (40) NOT NULL ,password VARCHAR (40)NOT NULL )
    ''')
cursor.execute("""
INSERT INTO account (personal_pin_code,email,username,password)
VALUES (1998,"Charlieaussie98@gmail.com","CharlieAussie98","Aussie98" )
""")
db.commit()
cursor.execute("SELECT * FROM account")
print(cursor.fetchall())
## hello dtt