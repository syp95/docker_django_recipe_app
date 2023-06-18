
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    
    def setUp(self):
        self.client = APIClient

    def test_유저_생성을_성공할_것이다(self):
        payload = {
            'email' : 'test@example.com',
            'password' : 'testpass123',
            'name' : 'test name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        assert res.status_code == status.HTTP_201_CREATED
        user = get_user_model().objects.get(email=payload['email'])
        assert user.check_password(payload['password']) == True
        assert not res.data['password']

    def test_이메일이_이미_존재하면_에러를_나타낼_것이다(self):
         payload = {
            'email' : 'test@example.com',
            'password' : 'testpass123',
            'name' : 'test name',
        }
         create_user(**payload)
         res = self.client.post(CREATE_USER_URL,payload)

         assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_비밀번호가_너무_짧으면_에러를_나타낼_것이다(self):
         payload = {
            'email' : 'test@example.com',
            'password' : 'pw',
            'name' : 'test name',
        }
         res = self.client.post(CREATE_USER_URL,payload)

         assert res.status_code == status.HTTP_400_BAD_REQUEST
         user_exists = get_user_model().objects.filter(email=payload['email'])
         assert user_exists == False