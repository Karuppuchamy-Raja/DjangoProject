from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    pro = list(reversed(Product.objects.all()))
    context={'pro':pro}
    return render(request, 'home.html', context)