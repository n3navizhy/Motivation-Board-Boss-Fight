import sqlite3 as sq
import csv
connection = sq.connect('database.db')

with open('kids.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ' ,quotechar=' ')
    with open('dbkids.sql') as db:
        for row in reader:
            connection.executescript(db.read())
            connection.execute('INSERT INTO kids (name, surname,points) VALUES (?, ?, ?)',
                         (row[1],row[0],row[2]))


curs = connection.cursor()
connection.commit()
connection.close()

