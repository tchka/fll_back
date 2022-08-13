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


class ExecutorLevel(models.Model):
    name = models.CharField("Уровень копирайтера", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уровень копирайтера"
        verbose_name_plural = "Уровни копирайтера"


class OrderStatus(models.Model):
    name = models.CharField("Статус", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    ORDER_TYPES = [
        ('1', 'Копирайтинг'),
        ('2', 'Маркетинг'),
        ('3', 'Веб разработка'),
        ('4', 'Рерайтиинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография')
    ]
    name = models.CharField("Заголовок", max_length=255)
    type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)
    description = models.TextField("Описание", blank=True)
    keyword = models.CharField("Ключевые слова", max_length=1023, blank=True)
    length = models.PositiveSmallIntegerField("Длина статьи", blank=True)
    execution_time = models.PositiveSmallIntegerField("Время выполнения", blank=True)
    price = models.PositiveSmallIntegerField("Цена", blank=True)
    executor_level = models.ForeignKey(ExecutorLevel, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, default=0, null=True)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Заказчик"
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="Исполнитель",
        blank=True,
        null=True
    )
    article = models.TextField("Текст статьи", blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{}, {}, price: {}'.format(self.name, self.get_type_display(), self.price)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказ"


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Отправитель")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Получатель")
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_edited = models.BooleanField(default=False)
    description = models.CharField(max_length=1023)


class Ticket(models.Model):
    SEVERITIES = [
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Высокая')
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Автор_тикета")
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    description = models.CharField(max_length=1023)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return '{}, {}, Is resolved? {}'.format(self.get_severity_display(), self.create_time, self.is_resolved)


class Review(models.Model):
    RATING_FILLED = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]

    rating = models.CharField(choices=RATING_FILLED, default='1', max_length=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Автор_отзыва")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Пользователь")
    description = models.CharField(max_length=1023)
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
