from unittest import TestCase

from mock import patch

from jaab.lib.db import get_company, get_employee, add_employee, \
    update_employee


class TestDB(TestCase):

    @patch("jaab.lib.db.companies")
    def test_get_company(self, companies):
        # Given a company id
        _id = 1

        # and i mock TinyDB companies collection
        company = {"id": _id}
        companies.get.return_value = company

        # When i call get_company
        result = get_company(_id)

        # Then the result have to be
        self.assertEquals(result, company)
        # And the method companies.get have to be called once
        self.assertEquals(companies.get.call_count, 1)

    @patch("jaab.lib.db.get_company")
    def test_get_employee(self, get_companies):
        # Given a company id and employee id
        _id = 1
        employee_id = 1

        # And i mock get_company with a company object
        company = {
            "id": _id,
            "employees": [
                {"name": "a"},
                {"name": "b"},
                {"name": "c"}
            ]
        }
        get_companies.return_value = company

        # When I call  get_employee
        result = get_employee(_id, employee_id)

        # Then the result have to be the second employee
        self.assertEquals(result, company.get("employees")[employee_id])
        # And the method get_company have to be called once
        self.assertEquals(get_companies.call_count, 1)
        # And has been called with the parameter company_id
        get_companies.assert_called_once_with(_id)

    @patch("jaab.lib.db.companies")
    @patch("jaab.lib.db.get_company")
    def test_add_employee(self, get_companies, companies):
        # Given a company id and employee
        _id = 1
        employee = {"name": "b"}

        # And i mock get_company with a company object
        company = {
            "id": _id,
            "employees": [
                {"name": "a"},
                {"name": "c"}
            ]
        }
        get_companies.return_value = company

        # And i mock the get_company function
        companies.update.return_value = {}

        # When I call add_employee
        result = add_employee(_id, employee)

        # Then the result have to be the new list of employee
        for e in company['employees'] + [employee]:
            self.assertIn(e, result)

        # And the method get_company have to be called once
        self.assertEquals(companies.update.call_count, 1)

    @patch("jaab.lib.db.companies")
    @patch("jaab.lib.db.get_company")
    def test_update_employee(self, get_companies, companies):
        # Given a company id and employee and an id
        _id = 1
        employee_id = 1
        employee = {"name": "bb"}

        # And i mock get_company with a company object
        company = {
            "id": _id,
            "employees": [
                {"name": "a"},
                {"name": "b"},
                {"name": "c"}
            ]
        }
        get_companies.return_value = company

        # And i mock the get_company function
        companies.update.return_value = {}

        # When I call add_employee
        result = update_employee(_id, employee_id, employee)

        # Then the second employee have to be the new one
        self.assertEquals(result[employee_id], employee)

        # And the method get_company have to be called once
        self.assertEquals(companies.update.call_count, 1)

