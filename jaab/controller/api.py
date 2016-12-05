from flask import jsonify, request

from jaab.lib import db

FORM_FIELDS = ["name", "role", "address", "tel", "email"]


def get_companies():
    try:
        companies = db.get_companies()
    except Exception as ex:
        return return_error(ex)
    return jsonify(companies)


def get_company(company_id):
    company = db.get_company(int(company_id))
    return jsonify(company)


def update_employee(company_id, employee_id=None):
    employee = request.json

    for f in FORM_FIELDS:
        if f not in employee:
            return ("Missing field %s" % f), 400

    try:
        if employee_id:
            employees = db.update_employee(
                int(company_id), int(employee_id), employee)
        else:
            employees = db.add_employee(int(company_id), employee)
    except Exception as ex:
        return return_error(ex)

    return jsonify(employees)


def get_employee(company_id, employee_id):
    try:
        employee = db.get_employee(int(company_id), int(employee_id))
    except Exception as ex:
        return return_error(ex)
    return jsonify(employee)


def delete_employee(company_id, employee_id):
    try:
        db.delete_employee(int(company_id), int(employee_id))
        company = db.get_company(company_id)
    except Exception as ex:
        return return_error(ex)
    return jsonify(company)


def return_error(ex):
    result = {
        "message": str(ex)
    }
    return jsonify(result), 500

