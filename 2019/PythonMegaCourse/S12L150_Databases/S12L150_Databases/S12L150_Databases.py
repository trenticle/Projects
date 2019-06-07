import sqlite3
import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='gunslinger' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='gunslinger' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

##insert('coffee cup',10,5)

##def view():
##    conn=psycopg2.connect('dbname="lite.db"')
##    cur=conn.cursor()
##    cur.execute('SELECT * FROM store')
##    rows=cur.fetchall()
##    conn.close()
##    return rows

##def delete(item):
##    conn=psycopg2.connect('dbname="lite.db"')
##    cur=conn.cursor()
##    cur.execute('DELETE FROM store WHERE item=?',(item,))
##    rows=cur.fetchall()
##    conn.commit()
##    conn.close()
##    return rows

##def update(quantity,price,item):
##    conn=psycopg2.connect('dbname="lite.db"')
##    cur=conn.cursor()
##    cur.execute('UPDATE store SET quantity=?,price=? WHERE item=?',(quantity,price,item))
##    rows=cur.fetchall()
##    conn.commit()
##    conn.close()
##    return rows

create_table()
insert("Apple",10,8.5)
##update(11,6,'water glass')
##print(view())




