from django.urls import path
from a import views

app_name = 'a'

urlpatterns = [
    path('', views.index, name='index'),
]
