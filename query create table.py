import sqlite3

con = sqlite3.connect("DBI.db")

cur = con.cursor()

cur.execute("""
            CREATE TABLE TBL1
            (col1 int,col2 text)
"""
)
con.commit()
