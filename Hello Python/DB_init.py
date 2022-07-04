import sqlite3 as sq

connection = sq.connect('database.db')


with open('dbkids.sql') as db:
    connection.executescript(db.read())

curs = connection.cursor()


connection.execute('INSERT INTO Boss ( hp,name,modelid) VALUES ("dodik",10000,01)')


connection.commit()
connection.close()

