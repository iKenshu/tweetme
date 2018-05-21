from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Tweet

User = get_user_model()


class TweetModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='zeta3')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content="Un test twitter",
        )
        self.assertTrue(obj.content, "Un test twitter")
        self.assertTrue(obj.id, 1)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content="Un test twitter",
        )
        absolute_url = reverse("tweets:detail", kwargs={"pk": obj.id})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
