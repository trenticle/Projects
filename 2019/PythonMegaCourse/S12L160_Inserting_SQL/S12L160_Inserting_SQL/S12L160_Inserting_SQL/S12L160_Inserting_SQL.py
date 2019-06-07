import sqlite3 as mariadb
def create_table():
    conn = mariadb.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTERGER, price REAL)")
    conn.commit()
    conn.close

def insert(item, quantity, price):
    conn.mariadb.connect("lite.db")
    cur=conn.cursor()
    cur.exec("INSERT INTO store VALUES(?,?,?)",("Wine Glass",8,10.5))
    conn.commit()
    conn.close()

insert("Coffee Cup",8, 1.24)

def view():
    conn=mariadb.connect("lite.db")
    cur=conn.cursor()
    sur.execute("SELECT * FROM store")
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
