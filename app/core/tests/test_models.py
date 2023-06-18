import pytest

from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status


class ModelTests(TestCase):
    def test_이메일과_비밀번호를_넣으면_유저를_생성할_것이다(self):
        email = "test@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        assert user.email == email
        assert user.check_password(password) == True
        # get = self.client.get("/user/")
        # assert get.status_code == status.HTTP_200_OK

    def test_새로운_유저_이메일_대소문자를_확인하고_소문자로_바꿀_것이다(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@Example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            assert user.email == expected

    def test_새로운_유저_생성시_이메일이_없으면_에러를_나타낼_것이다(self):
        with pytest.raises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_슈퍼유저가_생성될_것이다(self):
        user = get_user_model().objects.create_superuser(
            'test123.example.com',
            'test123',
        )

        assert user.is_superuser == True
        assert user.is_staff == True
