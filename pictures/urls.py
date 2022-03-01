from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('',views.all_img, name='all_images'),
  path('search/',views.search_results, name='search_results'),
  re_path('location/(/d+)',views.search_location,name='location')
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)