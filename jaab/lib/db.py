import os

from tinydb import TinyDB, where

from jaab import root_dir

DB = TinyDB(os.path.join(
    root_dir, 'resource/db/data.json'), default_table="companies")

companies = DB.table('companies')


def get_companies():
    return companies.all()


def get_company(company_id):
    company = companies.get(where('id') == company_id)
    return company


def get_employee(company_id, employee_id):
    employees = get_company(company_id)

    if employee_id < len(employees):
        return employees["employees"][employee_id]

    return None


def add_employee(company_id, employee):
    company = get_company(company_id)
    employees = company['employees']
    employees.append(employee)
    companies.update({"employees": employees}, where('id') == company_id)

    return employees


def update_employee(company_id, employee_id, employee):
    company = get_company(company_id)
    employees = company['employees']
    employees[employee_id] = employee

    companies.update({"employees": employees}, where('id') == company_id)

    return employees


def delete_employee(company_id, employee_id):

    employees = get_company(company_id)
    employees.pop(employee_id)

    companies.update({"employees": employees}, where('id') == company_id)

    return employees
