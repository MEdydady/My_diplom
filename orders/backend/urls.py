from django.urls import path
from django_rest_passwordreset.views import (reset_password_confirm,
                                             reset_password_request_token)

from backend.views import (AccountDetailsView, BasketView, CategoryView,
                           ConfirmAccountView, ContactView, LoginAccountView,
                           NewUserRegistrationView, OrderView, PartnerOrders,
                           PartnerState,PartnerUpdateView, ProductInfoView, ShopView)

app_name = "backend"
urlpatterns = [
    path("partner/update", PartnerUpdateView.as_view(), name="partner-update"),
    path("partner/status", PartnerState.as_view(), name="partner-status"),
    path("partner/orders", PartnerOrders.as_view(), name="partner-orders"),
    path("user/register", NewUserRegistrationView.as_view(), name="user-register"),
    # path(
    #     "user/register/confirm",
    #     ConfirmAccountView.as_view(),
    #     name="user-register-confirm",
    # ),
    path("user/details", AccountDetailsView.as_view(), name="user-details"),
    path("user/contact", ContactView.as_view(), name="user-contact"),
    path("user/login", LoginAccountView.as_view(), name="user-login"),
    # path("user/password_reset", reset_password_request_token, name="password-reset"),
    # path(
    #     "user/password_reset/confirm",
    #     reset_password_confirm,
    #     name="password-reset-confirm",
    # ),
    path("categories", CategoryView.as_view(), name="categories"),
    path("shops", ShopView.as_view(), name="shops"),
    path("products", ProductInfoView.as_view(), name="shops"),
    path("basket", BasketView.as_view(), name="basket"),
    path("order", OrderView.as_view(), name="order"),
]
