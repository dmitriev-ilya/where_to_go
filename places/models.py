from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200, unique=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    longitude = models.DecimalField('Долгота', max_digits=17, decimal_places=14)
    latitude = models.DecimalField('Широта', max_digits=17, decimal_places=14)

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Место'
        )
    image = models.ImageField('Изображение')
    sequence_number = models.IntegerField(
        'Порядковый номер изображения',
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ['sequence_number']

    def __str__(self) -> str:
        return f'{self.sequence_number} {self.place}'
