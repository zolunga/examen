from django.shortcuts import render
from .forms import *
from django.views.generic import TemplateView, DetailView
from .models import *

# Create your views here.


class registerView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()

        return render(request, 'register.html', {'form': form})


class indexView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'all_users.html', {})


class addUser(DetailView):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        ocupacion = request.GET.get('ocupacion', None)
        edad = request.GET.get('edad', None)
        escuela = request.GET.get('escuela', None)
        direccion = request.GET.get('direccion', None)
        actividades = request.GET.get('actividades', None)
        user = Usuarios(username, password)
        user.save()
        return render(request, 'all_users.html', {})


class deleteUser(DetailView):

    def get(self, request, *args, **kwargs):
       id = kwargs['id']
