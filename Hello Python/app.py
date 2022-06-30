import  sqlite3
from flask import Flask , render_template , request, url_for, flash, redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/',methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        print(request.form['title'])
        point(request.form['title'],200)
        return redirect(url_for('index'))
    conn = get_db_connection()
    kids = conn.execute('SELECT * FROM kids').fetchall()
    conn.close()
    return render_template('ind.html', kids=kids)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO kids (name, surname) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


def point(name,points):
    conn = get_db_connection()
    conn.execute('UPDATE kids SET "points" = "poinst" + ?'
                         ' WHERE name = ?',
                         (points,name))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run('localhost',4449)
    point("Rashid",100)
    




