from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import User,Asset
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class UserViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='testuser@mail.com',
            password='password1234',
            first_name='test',
            last_name='user',
            phone_number='1234567890',
            department='accounts',
            role='employee'
            )
        self.token=Token.objects.create(user=self.user)
        self.client.login(email='testuser@mail.com',password='password1234')

    def test_user_registration(self):
            url=reverse('register')
            data={
                'email':'testuser1@mail.com',
                'password':'password1234',
                'first_name':'test',
                'last_name':'user',
                'phone_number':'1234567890',
                'department':'tech',
                'role':'employee'
            }
            response=self.client.post(url,data,content_type='application/json')
            self.assertEqual(response.status_code,201)
    def test_user_login(self):
        url=reverse('login')
        data={
            'email':'testuser@mail.com',
            'password':'password1234'
            }
        response=self.client.post(url,data,content_type='application/json')
        self.assertIn('token',response.data)
        self.assertEqual(response.status_code,200)
    def test_user_details(self):
        url=reverse('user_details')
        response=self.client.get(url,headers={"Authorization": 'Token '+ self.token.key})
        self.assertEqual(response.data['email'],self.user.email)
        self.assertEqual(response.status_code,200)
    def test_user_list(self):
        url=reverse('all_users')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

class AssetViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='testadmin@mail.com',
            password='password1234',
            first_name='test',
            last_name='user',
            phone_number='1234567890',
            department='accounts',
            role='admin'
            )
        self.token=Token.objects.create(user=self.user)
        self.client.login(email='testuser@mail.com',password='password1234')
        self.asset=Asset.objects.create(
            name='test',
            description='test',
            serial_number='1234567890',
            category='tech',
            tag='test',
            status=True,
            asset_type='elctronic'
        )
    def test_add_asset(self):
        url=reverse('add_asset')
        data = {
            'name': 'New Asset',
            'description': 'Description for new asset',
            'serial_number': '0987654321',
            'category': 'office',
            'tag': 'new',
            'status': True,
            'asset_type': 'furniture'
        }
        response=self.client.post(url,data,headers={"Authorization": 'Token '+ self.token.key},content_type='application/json')
        self.assertEqual(response.status_code,201)
    def test_get_allassets(self):
        url=reverse('all_assets')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    import unittest
    unittest.main()