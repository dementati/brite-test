# coding: utf8
import json

from backend import test, resource


class TestResource(test.TestCase):

    def test_fetch(self):
        expected = json.loads('{"data": {"test": 123},"success": true}')
        obj = resource.Resource.fetch()
        self.assertEqual(obj, expected)


class TestResourceApi(test.TestCase):

    def test_fetch(self):
        expected = json.loads('{"data": {"test": 123},"success": true}')

        resp = self.api_mock.post("/api/resource.fetch")
        self.assertTrue(resp.get("error"))
        resp = self.api_mock.post("/api/user.create", dict(email="test@gmail.com", password="test"))
        self.assertEqual(resp.get("error"), None)
        resp = self.api_mock.post("/api/resource.fetch")
        self.assertEqual(resp, expected)
