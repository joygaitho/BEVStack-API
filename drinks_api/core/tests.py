from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, User


class CategoryAPITestCase(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="admin",
            password="adminpass",
            role="admin"
        )

        self.staff_user = User.objects.create_user(
            username="staff",
            password="staffpass",
            role="staff"
        )

        self.category = Category.objects.create(
            name="Coffee",
            description="Hot beverages"
        )

        self.list_url = reverse("category-list-create")
        self.detail_url = reverse(
            "category-detail", args=[self.category.id]
        )

    def test_staff_can_list_categories(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_staff_cannot_create_category(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post(
            self.list_url,
            {"name": "Tea"}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_category(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(
            self.list_url,
            {"name": "Juice"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

