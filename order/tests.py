from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from account.models import Profile

from .models import Category, ExecutorLevel, Order, OrderStatus

User = get_user_model()


class OrderApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer1",
            password="pass12345",
            email="customer1@test.local",
            fio="Заказчиков",
            role=1,
        )
        Profile.objects.create(user=self.user)
        self.category = Category.objects.create(name="Тексты", url="teksty")
        self.level = ExecutorLevel.objects.create(name="Новичок")
        self.draft = OrderStatus.objects.create(name="Черновик")

    def _login(self):
        login = self.client.post(
            "/auth/token/login",
            {"username": "customer1", "password": "pass12345"},
            format="json",
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"token {login.data['auth_token']}")

    def test_order_list_without_token_401(self):
        response = self.client.get("/api/order/all")
        self.assertEqual(response.status_code, 401)

    def test_create_order_without_token_401(self):
        response = self.client.post(
            "/api/order/new",
            {"name": "Статья", "customer": self.user.pk, "status": self.draft.pk},
            format="json",
        )
        self.assertEqual(response.status_code, 401)

    def test_create_order_with_token_201(self):
        self._login()
        response = self.client.post(
            "/api/order/new",
            {
                "name": "Статья про API",
                "category": "Тексты",
                "description": "Нужен текст",
                "keyword": "api",
                "length": 1000,
                "price": 500,
                "execution_time": 3,
                "executor_level": "Новичок",
                "customer": self.user.pk,
                "status": self.draft.pk,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().name, "Статья про API")
        self.assertEqual(Order.objects.get().customer_id, self.user.pk)
