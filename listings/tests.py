from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import requests

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




class JWTAuthTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('jwt-create')
    
    def test_jwt_create(self):
      

        # Test credentials (assuming you've created a user with these credentials)
        data = {
            'username': 'admin',
            'password': 'admin'
        }

        response = self.client.post(self.url, data=data)

        print(response.json())
        
        # Assert the status code (should be 200 OK for successful JWT creation)
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains a token
        self.assertIn('access', response.json())
        self.assertIn('refresh', response.json())
