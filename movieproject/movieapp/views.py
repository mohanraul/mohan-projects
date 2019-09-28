from django.shortcuts import render
from . import forms
from movieapp.models import Movie

# Create your views here.
def indexview(request):
    return render(request,'testapp/index.html')

def addview(request):
    form=forms.Movieform()
    if request.method=="POST":
        form=forms.Movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return indexview(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def listview(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movie_list':movie_list})
