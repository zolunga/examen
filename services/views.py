from django.shortcuts import render, redirect
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
        usuarios = Usuarios.objects.all()
        return render(request, 'all_users.html', {'users': usuarios})


class addUser(DetailView):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        ocupacion = request.GET.get('ocupacion', None)
        edad = request.GET.get('edad', None)
        email = request.GET.get('email', None)
        escuela = request.GET.get('escuela', None)
        direccion = request.GET.get('direccion', None)
        actividades = request.GET.get('actividades', None)
        extra = Extras(email=email, escuela=escuela, direccion=direccion)
        user = Usuarios(username=username, password=password)
        extra.save()
        user.save()
        return redirect('services:index')


class deleteUser(DetailView):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        print(id)
        return redirect('services:index')
