from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

def entries(request):
    template = loader.get_template('dashboard/entries.html')
    context = {}
    return HttpResponse(template.render(context,request))

def account(request):
    template = loader.get_template('dashboard/account.html')
    context = {}
    return HttpResponse(template.render(context,request))
