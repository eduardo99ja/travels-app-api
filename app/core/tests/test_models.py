from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime
from core import models


def sample_user(email='test@gmail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_travel_str(self):
        """Test the travel string representation"""
        travel = models.Travel.objects.create(
            user=sample_user(),
            title='Cancun',
            description='Visita Cancun',
            days=5,
            price=1500,
            category='Tour',
            location='Yucatan',
            departure_date=datetime.today(),
            countInStock=25
        )
        self.assertEqual(str(travel), travel.title)
