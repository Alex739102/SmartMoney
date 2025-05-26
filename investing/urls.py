from django.urls import path
from .views import flashcards_view

urlpatterns = [
    path('', flashcards_view, name='flashcards'),
]
