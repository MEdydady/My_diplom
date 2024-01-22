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
from django.core.mail import send_mail
from PIL import Image
from django.core.files import File
from backend.models import User
import tempfile


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
    

@shared_task
def upload_avatar(user_id, avatar_path):
    # Получите пользователя по ID
    user = User.objects.get(id=user_id)

    # Откройте изображение с использованием Pillow
    with Image.open(avatar_path) as img:
        # Сохраните изображение в файл
        with tempfile.NamedTemporaryFile(suffix=".jpg") as buffer:
            img.save(buffer, format="JPEG")
            buffer.seek(0)
            # Сохраните файл в поле аватара пользователя
            user.avatar.save(f"{user_id}.jpg", File(buffer), save=True)