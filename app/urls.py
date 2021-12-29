from django.conf.urls import static, url
from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('playcount',views.playcount, name='playcount'),
]
