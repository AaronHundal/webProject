from django.urls import path
from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
