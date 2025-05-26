from django.shortcuts import render
from .models import Flashcard

def flashcards_view(request):
    investing_cards = Flashcard.objects.filter(category='investing')
    trading_cards = Flashcard.objects.filter(category='trading')
    return render(request, 'flashcards.html', {
        'investing_cards': investing_cards,
        'trading_cards': trading_cards
    })
