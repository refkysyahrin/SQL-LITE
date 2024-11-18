import sqlite3

con = sqlite3.connect("DBI.db")

cur = con.cursor()

a=input('Masukan nomor: ')

b=input('Masukan nama: ')

cur.execute("""
            INSERT INTO TBL1 VALUES
            ({}, '{}')
""".format(a,b))

con.commit()
