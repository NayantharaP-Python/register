from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import Team


# Create your views here.
def demo(request):
    return HttpResponse("Hello")

def  demo(request):
    obj=place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'obj1':obj1})

