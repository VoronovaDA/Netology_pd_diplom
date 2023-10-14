import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from rest_framework.status import HTTP_200_OK
from django.urls import reverse


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def shop_factory():
    def factory(**kwargs):
        return baker.make("Shop", **kwargs)

    return factory


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return baker.make("Product", **kwargs)

    return factory


@pytest.fixture
def product_info_factory():
    def factory(**kwargs):
        return baker.make("ProductInfo", **kwargs)

    return factory


@pytest.fixture
def category_factory():
    def factory(**kwargs):
        return baker.make("Category", **kwargs)

    return factory


@pytest.mark.django_db
def test_get_shop(api_client, shop_factory):
    """Тест получения списка магазинов"""
    shop1 = shop_factory()
    shop2 = shop_factory()
    url = reverse("backend:shops")
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json["count"] == 2


@pytest.mark.django_db
def test_get_category(category_factory, api_client):
    """Тест на получение категории товаров"""
    category1 = category_factory()
    category2 = category_factory()
    url = reverse("backend:categories")
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json["count"] == 2
