import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK
from django.urls import reverse


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_client():
    User = get_user_model()
    user = User.objects.create_user(
        "seregina.0130@gmail.com",
        "pbkdf2_sha256$600000$XCHl3QA4MiiHrVj5EA3hzc$s4yp8FSgGucC83wioNDq4E0kxe5zUmLspKQs8VysQk0=",
    )
    token = Token.objects.get_or_create(user_id=user.id)
    list_token = list(token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + list_token[0].key)
    return client


@pytest.mark.django_db
def test_create_user(api_client, user_client):
    """Тест создания пользователя"""
    url = reverse("backend:user-register")
    user = {
        "first_name": "Darya",
        "last_name": "Voronova",
        "email": "seregina.0130@gmail.com",
        "password": "fevral33102318",
        "company": "KARMA",
        "position": "",
    }
    resp = api_client.post(url, user)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_confirm_account(api_client):
    """Тест подтверждения почтового адреса"""
    url = reverse("backend:user-register-confirm")
    user = {
        "email": "seregina.0130@gmail.com",
        "token": "2e1afe657e1f41da5b548bd08aa0d79a1195356b",
    }
    resp = api_client.post(url, user)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_login_account(api_client):
    """Тест авторизации пользователей"""
    url = reverse("backend:user-login")
    user = {
        "email": "seregina.0130@gmail.com",
        "password": "pbkdf2_sha256$600000$XCHl3QA4MiiHrVj5EA3hzc$s4yp8FSgGucC83wioNDq4E0kxe5zUmLspKQs8VysQk0=",
    }
    resp = api_client.post(url, user)
    assert resp.status_code == HTTP_200_OK
