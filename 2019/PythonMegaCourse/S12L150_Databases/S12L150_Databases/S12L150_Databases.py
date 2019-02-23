import sqlite3
import psycopg2

def create_table():
    conn=sqlite3.connect('d:\\Users\\trent\\Desktop\\New folder\\lite.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTERGER, price REAL)')
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect('d:\\Users\\trent\\Desktop\\New folder\\lite.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO store VALUES (?,?,?)',(item,quantity,price))
    conn.commit()
    conn.close()

insert('coffee cup',10,5)

def view():
    conn=sqlite3.connect('d:\\Users\\trent\\Desktop\\New folder\\lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect('d:\\Users\\trent\\Desktop\\New folder\\lite.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM store WHERE item=?',(item,))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(quantity,price,item):
    conn=sqlite3.connect('d:\\Users\\trent\\Desktop\\New folder\\lite.db')
    cur=conn.cursor()
    cur.execute('UPDATE store SET quantity=?,price=? WHERE item=?',(quantity,price,item))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

update(11,6,'water glass')
print(view())




