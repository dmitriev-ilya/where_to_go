from urllib.parse import urlparse, unquote

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load place description from JSON to Where_To_Go DataBase'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help='JSON file url'
        )

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_json = response.json()
        place, created = Place.objects.get_or_create(
            title=place_json['title'],
            defaults={
                'description_short': place_json.get('description_short', ''),
                'description_long': place_json.get('description_long', ''),
                'longitude': place_json['coordinates']['lng'],
                'latitude': place_json['coordinates']['lat'],
            },
        )
        if created:
            self.stdout.write('New place created in DataBase')
            self.stdout.write('Start images loading...')
            for image_url in place_json.get('imgs', []):
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                imagename = unquote(urlparse(image_url).path.split("/")[-1])
                image = Image.objects.create(place=place)
                with ContentFile(image_response.content) as image_content:
                    image.image.save(imagename, image_content, save=True)
            self.stdout.write('Complete!')
        else:
            self.stdout.write('This place existing in DataBase')
