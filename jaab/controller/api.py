from flask import jsonify, request

from jaab.lib import db

FORM_FIELDS = ["name", "role", "address", "tel", "email"]


def get_companies():
    compaines = db.get_companies()

    return jsonify(compaines)


def get_company(company_id):
    company = db.get_company(int(company_id))
    return jsonify(company)


def update_employee(company_id, employee_id=None):
    employee = request.json

    for f in FORM_FIELDS:
        if f not in employee:
            return ("Missing field %s" % f), 400

    if employee_id:
        employees = db.update_employee(
            int(company_id), int(employee_id), employee)
    else:
        employees = db.add_employee(int(company_id), employee)

    return jsonify(employees)


def get_employee(company_id, employee_id):
    employees = db.get_employee(int(company_id), int(employee_id))
    return jsonify(employees)


def delete_employee(company_id, employee_id):
    db.delete_employee(int(company_id), int(employee_id))
    return jsonify(True)
