from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index_page),
    path('places/<int:place_id>/', views.show_place_detail, name='json_place_detail'),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
