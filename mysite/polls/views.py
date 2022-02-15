from multiprocessing import context
from random import choice
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from .models import Poll



def index(request):
    context = { 'umfragen': Poll.objects.all(), 'titel': "Umfrageseite"}
    return render(request=request, template_name='polls/index.html',
                    context=context)
 
def umfrage_detail(request, slug):
    umfrage= get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request=request, template_name='polls/umfrage.html',
                    context=context)