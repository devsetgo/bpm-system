# -*- coding: utf-8 -*-
import unittest
import uuid

from async_asgi_testclient import TestClient

from main import app
from settings import config_settings

# from starlette.testclient import TestClient


client = TestClient(app)


class Test(unittest.TestCase):
    async def test_index(self):
        url = f"/"
        response = await client.get(url)
        assert response.status_code == 303

    async def test_login(self):

        data = {
            "user": config_settings.admin_user_name,
            "password": config_settings.admin_user_key,
        }
        url = f"/user/login"
        response = await client.post(url, data=data)
        assert response.status_code == 303

    async def test_health_pages(self):

        url = f"/health"
        response = await client.get(url)
        assert response.status_code == 200

    async def test_index_error(self):

        url = f"/{uuid.uuid1()}.html"
        response = await client.get(url)
        assert response.status_code == 303
