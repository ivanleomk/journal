from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.models import entry
from django.views.generic import TemplateView
import datetime
# Create your views here.


def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def entries(request):
    template = loader.get_template('dashboard/entries.html')
    entries = entry.objects.all()
    values = []
    for n in entries.values():
        date = n['entry_date'].strftime('%m/%d/%Y')
        values.append([date,n['entry']])
    print(values)
    entries = {'entry':values}
    return render(request, 'dashboard/entries.html', {"entries": values})

def account(request):
    template = loader.get_template('dashboard/account.html')
    context = {}
    return HttpResponse(template.render(context,request))

def newentry(request):
    template = loader.get_template('dashboard/newentry.html')
    context = {}
    return HttpResponse(template.render(context,request))
