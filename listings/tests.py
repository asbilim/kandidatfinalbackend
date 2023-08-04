from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserCreationTest(APITestCase):
    def setUp(self):
        self.url = reverse('user-create-list')

    def test_user_creation_success(self):
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['content'], 'user created successfully')
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_user_creation_error(self):
        # Creating a user with an empty username and password, which should trigger an error
        data = {'username': '', 'password': ''}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')
        self.assertEqual(response.data['content'], 'An error occurred while creating the user!')
        self.assertFalse(get_user_model().objects.filter(username='').exists())
