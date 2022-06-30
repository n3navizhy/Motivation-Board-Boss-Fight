import sqlite3 as sq

connection = sq.connect('database.db')


with open('dbkids.sql') as db:
    connection.executescript(db.read())

curs = connection.cursor()


connection.commit()
connection.close()

