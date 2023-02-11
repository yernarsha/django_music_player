from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Song
from .forms import SongForm

# Create your views here.

def home(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "playerapp/index.html", {"page_obj": page_obj})

def add(request):
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors.as_data())
            return render(request, "playerapp/add_song.html", {'form': form})
        
    else:
        form = SongForm()      
        songs = Song.objects.all()

    return render(request, "playerapp/add_song.html", {'form': form, 'songs': songs})

