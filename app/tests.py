from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.test.utils import CaptureQueriesContext
from django.db import connection
from rest_framework import status

from app.models import BlogPost, Comment

User = get_user_model()


class PostAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.client = APIClient()

        cls.user = User.objects.create_user(
            username="test",
            password="1234"
        )
        response = cls.client.post("/api/token/", {"username": "test", "password": "1234"})
        cls.access_token = response.data["access"]

        # 建立測試資料
        for i in range(10):

            cls.post = BlogPost.objects.create(
                title=f"title{i}",
                subtitle="subtitle",
                date="2026-03-08",
                body="body",
                author=cls.user,
                img_url="img"
            )

            for j in range(5):
                Comment.objects.create(
                    text="comment",
                    comment_author=cls.user,
                    parent_post=cls.post
                )

    def test_post_list_query_count(self):

        with CaptureQueriesContext(connection) as queries:

            response = self.client.get("/api/post/")

            self.assertEqual(response.status_code, 200)

        print("SQL count:", len(queries))

        # 如果 N+1 就會超過
        self.assertLess(len(queries), 5)

    def test_author_can_edit_post(self):

        self.client.force_authenticate(self.user)

        response = self.client.patch(
            f"/api/post/{self.post.id}/",
            {"title": "updated"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_list_posts(self):

        response = self.client.get("/api/post/")

        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):

        self.client.force_authenticate(self.user)

        response = self.client.delete(
            f"/api/post/{self.post.id}/"
        )

        self.assertEqual(response.status_code, 204)

    def test_jwt_login(self):

        User.objects.create_user(
            username="frank",
            password="123456"
        )

        response = self.client.post(
            "/api/token/",
            {
                "username": "frank",
                "password": "123456"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_access_protected_api(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        response = self.client.get("/api/post/")

        self.assertEqual(response.status_code, 200)