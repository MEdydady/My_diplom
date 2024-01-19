from backend.models import (
    Category,
    Parameter,
    Product,
    ProductInfo,
    ProductParameter,
    Shop,
)
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail



@shared_task()
def send_email_task(user_email,message):
    # send email to user
    send_mail(
        # title:
        f"Password Reset Token for {user_email}",
        # message:
        f"{message}",
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user_email],
        fail_silently=False,
    )