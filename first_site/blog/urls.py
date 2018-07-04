from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil/', views.home),
    url(r'^arct/<id_arct>', views.arct),
]