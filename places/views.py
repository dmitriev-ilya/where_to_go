from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def show_index_page(request):
    context = {
        'place_descriptions': {
            'type': 'FeatureCollection',
            'features': []
        }
    }

    places = Place.objects.all()
    for place in places:
        place_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('json_place_detail', args=[place.id])
            }
        }
        context['place_descriptions']['features'].append(place_feature)

    return render(request, 'index.html', context=context)


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {
        'title': place.title,
        'imgs': [item.image.url for item in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
