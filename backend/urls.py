from django.urls import path
from django_rest_passwordreset.views import (
    reset_password_request_token,
    reset_password_confirm,
)

from backend.views import (
    UserRegisterView,
    PartnerUpdate,
    LoginAccount,
    CategoryView,
    ShopView,
    ProductInfoView,
    BasketView,
    ContactView,
    OrderView,
    PartnerState,
    PartnerOrders,
    ConfirmAccount,
)

app_name = "backend"
urlpatterns = [
    path("user/register", UserRegisterView.as_view(), name="user-register"),
    path(
        "user/register/confirm", ConfirmAccount.as_view(), name="user-register-confirm"
    ),
    path("user/login", LoginAccount.as_view(), name="user-login"),
    path("user/password_reset", reset_password_request_token, name="password-reset"),
    path(
        "user/password_reset/confirm",
        reset_password_confirm,
        name="password-reset-confirm",
    ),
    path("user/contact", ContactView.as_view(), name="user-contact"),
    path("partner/update", PartnerUpdate.as_view(), name="partner-update"),
    path("partner/state", PartnerState.as_view(), name="partner-state"),
    path("partner/orders", PartnerOrders.as_view(), name="partner-orders"),
    path("categories", CategoryView.as_view(), name="categories"),
    path("shops", ShopView.as_view(), name="shops"),
    path("products", ProductInfoView.as_view(), name="shops"),
    path("basket", BasketView.as_view(), name="basket"),
    path("order", OrderView.as_view(), name="order"),
]
