# python
import json

# django
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# django contrib
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# libs

# project


def home_view(request):

    return render(request, 'home.html', {
    })


def register_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('register_done'))
    return render(request, 'register_user.html', {
        'form': form,
    })


def register_done(request):
    return render(request, 'register_done.html')
