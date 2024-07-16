from datetime import *

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone
import pytz

from config import settings
from users.models import User


@shared_task
def check_last_login():
    """
    Блокирует пользователя, если он не входил в систему более 30 дней
    """
    users = User.objects.filter(is_active=True)
    for user in users:
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
