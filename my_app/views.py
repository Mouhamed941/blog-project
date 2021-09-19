from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from my_app.models import Horse
# Create your views here.



from django.views import generic
class HorseList(generic.ListView):
    model = Horse    


class HorseDetail(ListView):
    model = Horse