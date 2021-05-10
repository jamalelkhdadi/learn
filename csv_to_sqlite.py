import csv
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("create table if not exists terms (name text, value text)")

with open('file.csv', 'r') as fin:

    dr = csv.DictReader(fin)
    to_db = [(i['name'], i['value']) for i in dr]

cur.executemany("INSERT INTO terms (name, value) VALUES (?, ?);", to_db)

con.commit()
con.close()
