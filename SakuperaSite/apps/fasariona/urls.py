from django.urls import path
from .views import *

app_name = 'fasariona'

urlpatterns = [
    path("", index, name='index'),
    path("dictionary/", dictionary, name='dictionary'),
    path("dictionary/<int:pk>", dictionary_detail, name='dictionary_detail'),
    path("gwiki/", gwiki, name='gwiki'),
    path("gwiki/<int:pk>/", gwiki_detail, name='gwiki_detail'),
]
