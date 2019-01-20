from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dashboard.models import entry
from django.views.generic import TemplateView
import datetime
from .models import entry
# Create your views here.

#Main Dashboard page
def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

#Entries Page
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

#Account Page
def account(request):
    template = loader.get_template('dashboard/account.html')
    context = {}
    return HttpResponse(template.render(context,request))

#New Entry!
def newentry(request):
    template = loader.get_template('dashboard/newentry.html')
    if request.method == 'POST':
        if request.POST.get('entry'):
            post=entry()
            post.entry= request.POST.get('entry')
            post.save()
            return render(request, 'dashboard/index.html')
        else:
            return render(request,'dashboard/entries.html')
    else:
        return render(request,'dashboard/newentry.html')
