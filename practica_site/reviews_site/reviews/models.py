from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE, verbose_name="Ресторан")
    author = models.CharField(max_length=100, verbose_name="Автор")
    rating = models.PositiveIntegerField(verbose_name="Оценка")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отзыв от {self.author} для {self.restaurant.name}"
