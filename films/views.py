from django.shortcuts import render
from .models import Film
from django.db.models import Q
from django.views.generic import DetailView
# Create your views here.
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        film = Film.objects.filter(Q(title__icontains=q)).order_by('-id') 
    else:
        film = Film.objects.all().order_by('-id')
    
    return render(request,'list.html',{'film':film})

class detail(DetailView):
    model = Film
    template_name = 'detail.html'
