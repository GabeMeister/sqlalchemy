# pylint: disable=C0111,C0103


import random
import requests


def get_names(amount):
    assert amount > 0 and amount <= 500, 'Amount must be > 0 and <= 500'

    url_str = 'https://uinames.com/api/?region=United States&amount={0}'.format(amount)
    resp = requests.get(url_str)
    return resp.json()


def get_zip_numbers(amount):
    assert amount > 0 and amount <= 500, 'Amount must be > 0 and <= 500'

    zips = []
    for _ in range(0, amount):
        zips.append(str(random.randrange(10000, 99999)))

    return zips


def get_street_names(amount):
    assert amount > 0 and amount <= 500, 'Amount must be > 0 and <= 500'

    street_types = ['Ln', 'St', 'Ct', 'Dr', 'Blvd', 'Way']
    street_types_count = len(street_types)

    url_str = 'https://uinames.com/api/?region=United States&amount={0}'.format(amount)
    resp = requests.get(url_str)

    street_names = []
    for item in resp.json():
        rand_street_type = street_types[random.randrange(0, street_types_count)]
        street_names.append('{0} {1}'.format(item['name'], rand_street_type))

    return street_names


def get_street_numbers(amount):
    assert amount > 0 and amount <= 500, 'Amount must be > 0 and <= 500'

    street_numbers = []
    for _ in range(0, amount):
        street_numbers.append(random.randrange(10, 999))

    return street_numbers
