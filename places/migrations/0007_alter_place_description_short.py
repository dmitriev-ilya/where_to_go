# Generated by Django 4.1.7 on 2023-04-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]
