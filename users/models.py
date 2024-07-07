from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя
    """

    name = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=20, verbose_name="телефон", **NULLABLE)
    city = models.CharField(max_length=20, verbose_name="город", **NULLABLE)
    image = models.ImageField(upload_to="user", verbose_name="аватар", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payments(models.Model):
    """
    Модель оплаты
    """

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    course = models.ForeignKey(
        to=Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE
    )
    lesson = models.ForeignKey(
        to=Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE
    )
    payment = models.FloatField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=150, verbose_name="Способ оплаты")

    def __str__(self):
        return f"{self.user} - {self.course if self.course else self.lesson} : {self.payment}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"
        ordering = ("-payment_date",)
