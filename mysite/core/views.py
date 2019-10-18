from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .forms import PontoTuristicoForm
from django.http import JsonResponse



def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

def add_new_point_view(request):
    if request.method == "POST":
        form = PontoTuristicoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return JsonResponse({'msg': 'Data saved'})
        else:
            print("ERROR FORM INVALID")
            return JsonResponse({'msg': 'ERROR FORM INVALID'})
    else:
        form = PontoTuristicoForm()
    return JsonResponse({'form': form})    
