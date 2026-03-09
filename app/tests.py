from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse
from django.test.utils import CaptureQueriesContext
from django.db import connection

from app.models import BlogPost, Comment

User = get_user_model()


class PostAPITest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.client = APIClient()

        cls.user = User.objects.create_user(
            username="test",
            password="1234"
        )

        # 建立測試資料
        for i in range(10):

            post = BlogPost.objects.create(
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
                    parent_post=post
                )

    def test_post_list_query_count(self):

        with CaptureQueriesContext(connection) as queries:

            response = self.client.get("/api/post/")

            self.assertEqual(response.status_code, 200)

        print("SQL count:", len(queries))

        # 如果 N+1 就會超過
        self.assertLess(len(queries), 5)