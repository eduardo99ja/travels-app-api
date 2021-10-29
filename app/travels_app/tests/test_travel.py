
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


from rest_framework.test import APIClient


TRAVEL_CREATE_URL = reverse('travel-create')


class PublicTravelApiTests(TestCase):
    """Test unauthenticated recipe API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test that authentication is required"""
        res = self.client.get(TRAVEL_CREATE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTravelApiTests(TestCase):
    """Test authenticated recipe API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)
        # self.token = Token.objects.create(user=self.user)

        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_basic_recipe(self):
        """Test creating recipe"""
        payload = {
            "title": "Cancun 2",
            "description": "Visita Cancun",
            "days": 5,
            "price": 5000,
            "category": "Tours",
            "location": "Yucatan",
            "departure_date": "2021-10-10",
            "countInStock": 25
        }
        res = self.client.post(TRAVEL_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
