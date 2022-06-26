from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField("Категория", max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CopyrighterLevel(models.Model):
    name = models.CharField("Уровень копирайтера", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уровень копирайтера"
        verbose_name_plural = "Уровни копирайтера"


class JobStatus(models.Model):
    name = models.CharField("Статус", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Job(models.Model):
    name = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", blank=True)
    keyword = models.CharField("Ключевые слова", max_length=1023, blank=True)
    length = models.PositiveSmallIntegerField("Длина статьи", blank=True)
    execution_time = models.PositiveSmallIntegerField("Время выполнения", blank=True)
    price = models.PositiveSmallIntegerField("Цена", blank=True)
    copyrighter_level = models.ForeignKey(CopyrighterLevel, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(JobStatus, on_delete=models.SET_NULL, default=0, null=True)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = "Заказчик"
    )
    copyrighter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name = "Копирайтер",
        blank=True,
        null=True
    )
    article = models.TextField("Текст статьи", blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
