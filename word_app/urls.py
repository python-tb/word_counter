
from django.urls import path
from word_app import views

urlpatterns = [
    path('', views.index,name='home'),
    path('chars', views.chars,name='chars'),
    path('vowels', views.vowels,name='vowels'),
    path('consonants', views.consonants,name='consonants'),
    path('upper', views.upper,name='upper'),
    path('lower', views.lower,name='lower'),
]