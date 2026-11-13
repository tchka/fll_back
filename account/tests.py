from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from .models import Profile

User = get_user_model()


class AccountApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer1",
            password="pass12345",
            email="customer1@test.local",
            fio="Заказчиков",
            role=1,
        )
        Profile.objects.create(user=self.user)

    def test_account_without_token_401(self):
        response = self.client.get(f"/api/account/{self.user.pk}")
        self.assertEqual(response.status_code, 401)

    def test_login_returns_token(self):
        response = self.client.post(
            "/auth/token/login",
            {"username": "customer1", "password": "pass12345"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("auth_token", response.data)

    def test_login_wrong_password(self):
        response = self.client.post(
            "/auth/token/login",
            {"username": "customer1", "password": "wrong"},
            format="json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertNotIn("auth_token", response.data)

    def test_account_with_token_200(self):
        login = self.client.post(
            "/auth/token/login",
            {"username": "customer1", "password": "pass12345"},
            format="json",
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"token {login.data['auth_token']}")
        response = self.client.get(f"/api/account/{self.user.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "customer1")
