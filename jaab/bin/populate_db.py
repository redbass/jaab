import random

from faker import Factory

from jaab.lib.db import DB, companies

fake = Factory.create()

DB.purge_tables()


def create_company(_id):

    rnd_employee = random.randint(5, 20)

    company = {
        "id": _id,
        "name": fake.company(),
        "description": fake.text(max_nb_chars=100),
        "tel": fake.phone_number(),
        "email": fake.email(),
        "address": fake.address(),
        "employees": [create_employee() for e in xrange(0, rnd_employee)]
    }

    companies.insert(company)


def create_employee():
    return {
        "name": fake.name(),
        "role": fake.job(),
        "tel": fake.phone_number(),
        "email": fake.email(),
        "address": fake.address()
    }


for i in xrange(0, 20):
    create_company(i)
