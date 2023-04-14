from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200, blank=False)
    description_short = models.CharField('Краткое описание', max_length=300)
    description_long = models.TextField('Полное описание')
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
    sequence_number = models.IntegerField('Порядковый номер изображения', default=1)

    def __str__(self) -> str:
        return f'{self.sequence_number} {self.place}'