from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200, blank=False)
    description_short = models.CharField('Краткое описание', max_length=300)
    description_long = models.TextField('Полное описание')
    longitude = models.DecimalField('Долгота', max_digits=17, decimal_places=14)
    latitude = models.DecimalField('Широта', max_digits=17, decimal_places=14)

    def __str__(self) -> str:
        return self.title