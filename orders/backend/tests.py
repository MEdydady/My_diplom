from django.test import TestCase
import pytest
from rest_framework.test import APIRequestFactory, APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .views import NewUserRegistrationView
# Create your tests here.

@pytest.mark.django_db
def test_new_user_registration():
    factory = APIRequestFactory()
    view = NewUserRegistrationView.as_view()
    client = APIClient()

    user_model = get_user_model()
    user_count = user_model.objects.count()

    request = factory.post('http://127.0.0.1:8000/api/v1/user/register', {
        'username': 'testuser',
        'password': 'testpassword123',
        'email': 'testuser@example.com',
    })
    response = view(request)

    assert response.status_code == 201
    assert user_model.objects.count() == user_count + 1
    assert response.data['status'] == 'Success'
    assert response.data['message'] == 'Учетная запись создана, на почту отправлен токен'
    assert 'token' in response.data

    # new_user = user_model.objects.latest('id')
    # token = Token.objects.get(user=new_user)
    # assert response.data['token'] == {token.key}