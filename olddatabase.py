# pylint: disable=C0111,C0103


import sqlite3


def create_db_old_way():
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()

    c.execute('CREATE TABLE person (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)')

    c.execute('''
    CREATE TABLE address
  
        id INTEGER PRIMARY KEY ASC,
        street_name varchar(250),
        street_number varchar(250),
        post_code varchar(250) NOT NULL,
        person_id INTEGER NOT NULL,
        FOREIGN KEY(person_id) REFERENCES person(id)
    )
    ''')

    c.execute('''
    INSERT INTO person VALUES (1, 'Gabe Jensen')
    ''')

    c.execute('''
    INSERT INTO address VALUES (1, 'Unicorn Ln', '999', '99453', 1)
    ''')

    conn.commit()
    conn.close()


def select_from_db_old_way():
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()

    c.execute('SELECT * FROM person')

    data = c.fetchall()
    print data
    print 'Type of data: ' + str(type(data))

    c.execute('SELECT * FROM address')

    print c.fetchall()
