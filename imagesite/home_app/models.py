from django.db import models


# кастомный менеджер фильтрации опубликованных инстансов
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=SliderImage.Status.PUBLISHED)


class SliderImage(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Скрыто'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Изображение')
    upload = models.ImageField(upload_to='media')
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    published = PublishedManager()
    # что бы вернуть стандарный менеджер
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_update']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
