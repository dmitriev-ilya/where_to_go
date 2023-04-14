from django.shortcuts import render

from places.models import Place


def show_index_page(request):
    context = {
        'place_descriptions': {
            "type": "FeatureCollection",
            "features": []
        }    
    }

    places = Place.objects.all()
    for place in places:
        place_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "coming_soon"
            }
        }
        context['place_descriptions']['features'].append(place_feature)

    return render(request, 'index.html', context=context)
