# pylint: disable=C0111,C0103,E1101

import os
import generator
# from datetime import datetime
# from faker import Faker
from models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_FILE_NAME = 'tutorial.db'
DB_URI = 'sqlite:///{0}'.format(DB_FILE_NAME)

Engine = create_engine(DB_URI)
Base.metadata.bind = Engine
DBSession = sessionmaker(bind=Engine)


def create_db():
    Base.metadata.create_all(Engine)


def delete_db():
    if os.path.isfile(DB_FILE_NAME):
        os.remove(DB_FILE_NAME)


def insert_db(amount):
    assert amount > 0 and amount <= 500, 'Amount must be > 0 and <= 500'

    session = DBSession()

    names = generator.get_names(amount)
    zips = generator.get_zip_numbers(amount)
    street_names = generator.get_street_names(amount)
    street_numbers = generator.get_street_numbers(amount)

    for i in range(0, amount):
        full_name = '{0} {1}'.format(names[i]['name'], names[i]['surname'])
        new_person = Person(name=full_name)
        session.add(new_person)

        new_address = Address(street_number=street_numbers[i],\
            street_name=street_names[i],\
            post_code=zips[i])
        new_address.person = new_person
        session.add(new_address)

    session.commit()

def select_db(name):
    assert name != '', 'Must supply string name'

    session = DBSession()

    query = session.query(Person).filter(Person.name.contains('Fe'))
    print query

    people = query.all()
    for person in people:
        print person

    # addresses = session.query(Address).filter(Address.person == person).all()
    # print addresses[0]


def do_sandbox_test():
    session = DBSession()

    my_user = User(name=98, age='2', is_admin='')
    session.add(my_user)
    session.commit()

    new_user = session.query(User).filter(User.age == 200).first()
    if my_user.name == new_user.name:
        print 'yup!'
    else:
        print 'nope.'

    print 'my_user.id: ' + str(my_user.id)
    print 'new_user.id: ' + str(new_user.id)



