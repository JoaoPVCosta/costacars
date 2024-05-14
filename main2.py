import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('Stand.db')

c = conn.cursor()
try:
    c.execute("""CREATE TABLE Cars (
    id integer PRIMARY KEY,
    brand varchar(50),
    model varchar(50),
    year integer,
    kms integer,
    hp integer,
    price float,
    color varchar(50),
    doors integer
    )""")

except sqlite3.OperationalError:
    print("This table already exists.")

try:
    fake = Faker(['pt_PT'])
    for i in range(10):
        brand = fake.company()
        model = fake.word()
        year = random.randint(1950, 2021)
        kms = random.randint(0, 200000)
        hp = random.randint(50, 450)
        price = random.randint(5000, 50000)
        color = fake.color_name()
        doors = random.randint(3, 5)
        c.execute(f"""INSERT INTO Cars (id, brand, model, year, kms, hp, price, color, doors) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (i, brand, model, year, kms, hp, price, color, doors))

except sqlite3.IntegrityError:
    print("This car already exists.")

c.execute("""SELECT * FROM Cars""")

data = c.fetchone()
print(data)

data = c.fetchone()
print(data)

print("--" * 10)

data = c.fetchmany(3)
for row in data:
    print(row)

d = c.fetchall()
for row in d:
    print(row)

conn.commit()
conn.close()