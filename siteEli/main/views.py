from django.shortcuts import render
from .models import Song

# Create your views here.

def index(request):
    allSongs = Song.objects.all()
    currentSong = Song.objects.get(id=1)
    return render(request, 'main/index.html', {'allSongs': allSongs, 'currentSong': currentSong})

def song(request, id):
    allSongs = Song.objects.all()
    currentSong = Song.objects.get(id=id)
    return render(request, 'main/index.html', {'allSongs': allSongs, 'currentSong': currentSong})