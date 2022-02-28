from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('',views.welcome, name='welcome'),
  path('today/',views.test, name='testing'),
  path('kesho/',views.amazing, name='testing2')
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)