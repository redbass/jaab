import json
from unittest import TestCase

from flask import url_for
from mock import patch

from jaab.app import jaab_app
from jaab.lib.route import set_routes


class TestAPI(TestCase):

    def setUp(self):
        super(TestAPI, self).setUp()
        set_routes(jaab_app)
        self.client = jaab_app.test_client()

    @patch("jaab.controller.api.db")
    def test_get_companies(self, db):
        # Given that i mock get_companies function
        companies = [
            {"id": 0, "name": "c1"},
            {"id": 1, "name": "c2"},
            {"id": 2, "name": "c3"}
        ]
        db.get_companies.return_value = companies

        # When im calling the endpoint get_companies
        with self.client as client:
            response = client.get("/api/v1/company")

        # Then the response have to be the the given array
        self.assertEquals(json.loads(response.data), companies)

    @patch("jaab.controller.api.db")
    def test_get_company(self, db):
        # Given that i mock get_companies function
        _id = 0
        company = {"id": _id, "name": "c1"}
        db.get_company.return_value = company

        # When im calling the endpoint get_company
        with self.client as client:
            response = client.get("/api/v1/company/" + str(_id))

        # Then the response have to be the the given company
        self.assertEquals(json.loads(response.data), company)

        # And the function get_company have to be call with
        db.get_company.assert_called_once_with(int(_id))

    @patch("jaab.controller.api.db")
    def test_get_employee(self, db):
        # Given that i mock get_employee function
        _id = 0
        _eid = 0
        employee = {"name": "e1"}
        db.get_employee.return_value = employee

        # When im calling the endpoint get_company
        with self.client as client:
            response = client.get("/api/v1/company/%s/employee/%s" %
                                  (_id, _eid))

        # Then the response have to be the the given employee
        self.assertEquals(json.loads(response.data), employee)

        # And the function get_employee have to be call with
        db.get_employee.assert_called_once_with(int(_id), int(_eid))

    @patch("jaab.controller.api.db")
    def test_delete_employee(self, db):
        # Given that i mock get_company function
        _id = 0
        _eid = 0
        company = {
            "name": "c1",
            "employees": [
                {"name": "e1"}
            ]
        }
        db.get_company.return_value = company

        # When im calling the endpoint get_company
        with self.client as client:
            response = client.delete("/api/v1/company/%s/employee/%s" %
                                     (_id, _eid))

        # Then the response have to be the the given employee
        self.assertEquals(json.loads(response.data), company)

        # And the function get_employee have to be call with
        db.delete_employee.assert_called_once_with(int(_id), int(_eid))
