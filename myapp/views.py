from django.shortcuts import render

# Create your views here.
from . models import Mutlipleimg

def upload(request) : 
    if request.method == 'POST' : 
        images = request.FILES.getlist('images')
        for i in images : 
            Mutlipleimg.objects.create(images=i)

    images = Mutlipleimg.objects.all()
    return render(request , 'index.html' , {'images' : images})