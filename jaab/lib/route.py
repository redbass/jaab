from jaab.controller.api import get_companies, get_company, get_employee, \
    update_employee, delete_employee
from jaab.controller.ui import jaab, get_template


def set_routes(app):

    app.add_url_rule("/", endpoint="app", view_func=jaab)

    app.add_url_rule("/templates/<name>.html", endpoint="templates",
                     view_func=get_template, methods=["GET"])

    # API
    # Companies
    app.add_url_rule("/api/v1/company", endpoint="api.get_companies",
                     view_func=get_companies, methods=["GET"])

    # Employees
    app.add_url_rule("/api/v1/company/<company_id>", methods=["GET"],
                     endpoint="api.get_company", view_func=get_company)

    app.add_url_rule("/api/v1/company/<company_id>/employee",
                     methods=["POST"], endpoint="api.add_employee",
                     view_func=update_employee)

    # Employee
    app.add_url_rule("/api/v1/company/<company_id>/employee/<employee_id>",
                     methods=["POST"], endpoint="api.update_employee",
                     view_func=update_employee)

    app.add_url_rule("/api/v1/company/<company_id>/employee/<employee_id>",
                     methods=["DELETE"], endpoint="api.delete_employee",
                     view_func=delete_employee)

    app.add_url_rule("/api/v1/company/<company_id>/employee/<employee_id>",
                     endpoint="api.get_employee", view_func=get_employee,
                     methods=["GET"])
