from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.models import entry

# Create your views here.


def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

def entries(request):
    template = loader.get_template('dashboard/entries.html')
    entries = entry.objects.all()
    content = {}
    #context = {[1,"today was a good day","12-03-17"],[2,"today was an good day","12-03-17"],[3,"today was and good day","12-03-17"]}
    return HttpResponse(template.render(context,request))

def account(request):
    template = loader.get_template('dashboard/account.html')
    context = {}
    return HttpResponse(template.render(context,request))

def newentry(request):
    template = loader.get_template('dashboard/newentry.html')
    context = {}
    return HttpResponse(template.render(context,request))
