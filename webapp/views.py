import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from .models import peoples
from .form import NameForm


def get_data(request):
    if request.method == 'POST':
        form=NameForm(request.POST)
        if form.is_valid():
            obj = peoples()
            obj.userName = form.cleaned_data['userName']
            obj.emailid = form.cleaned_data['emailid']
            obj.phoneNo = form.cleaned_data['phoneNo']
            obj.password = form.cleaned_data['password']
            #obj.datetime = form.cleaned_data['datetime']
            obj.save()
            return HttpResponseRedirect('/')

    else:
        form=NameForm()
    return render(request, 'form.htm', {'form': form})


def index(request):
    form=NameForm()
    return render(request, 'form.htm', {'form': form})



def helloworld(request):
    return render(request, 'hello.html')
