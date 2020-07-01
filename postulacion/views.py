from django.shortcuts import render
from .forms import PostulantesForm


# Create your views here.

def home(request):
    form = PostulantesForm()
    return render(request, 'base.html', {'form': form})
