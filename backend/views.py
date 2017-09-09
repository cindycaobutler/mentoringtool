from django.shortcuts import render
from django.http import HttpResponse
from models import *

def home(request):
    context = {}
    context['home'] = 'Home page'
    return render(request, 'home.html', context)

def test(request):
    context = {}
    context['queryresults'] = User_data.objects.all()
    return render(request, 'test.html', context)

def testview(request):
    testuser = User_data(name='duoqi',
                      location='12345 Chase Rd apt.123')
    testuser.save()
    return HttpResponse("<h1>Saved!</h1>")