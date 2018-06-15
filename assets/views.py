from django.shortcuts import render
from .models import CloudManufacturer
# Create your views here.


def home(request):
    manufacturers = CloudManufacturer.objects.all()
    return render(request, 'manufacturers.html', {'manufacturers': manufacturers})
