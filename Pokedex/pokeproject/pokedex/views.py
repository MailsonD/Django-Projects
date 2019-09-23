from django.shortcuts import render
from .models import Pokemon


# Create your views here.

def home(request):
    pokemon_list = Pokemon.objects.all()
    return render(request, "pokedex/pokemon.html", {"pokemon_list": pokemon_list})
