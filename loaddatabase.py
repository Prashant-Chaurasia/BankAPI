import psycopg2
import csv
conn = psycopg2.connect("host=localhost dbname=bank user=bank password=bank")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS bank_branches CASCADE ")

cur.execute("""
            CREATE TABLE bank_branches(
              ifsc        VARCHAR(50) NOT NULL PRIMARY KEY,
              bank_id     INTEGER NOT NULL,
              branch      VARCHAR(100),
              address     VARCHAR(300),
              city        VARCHAR (50),
              district    VARCHAR (50),
              state       VARCHAR (50),
              bank_name   VARCHAR (200)
            )
""")

with open('bank_branches.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO bank_branches VALUES( %s, %s, %s, %s, %s,%s, %s,%s)",row

        )
conn.commit()