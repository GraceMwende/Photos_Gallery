from django.urls import path,re_path
from . import views

urlpatterns = [
  path('',views.welcome, name='welcome'),
  path('today/',views.test, name='testing'),
  path('kesho/',views.amazing, name='testing2'),
  re_path('archives/(\d{4}-\d{2})/',views.wuueh, name='testing')
]