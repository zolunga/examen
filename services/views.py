from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import TemplateView, DetailView
from .models import *
from rest_framework import serializers, viewsets

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
        try:
            username = request.GET.get('username', None)
            password = request.GET.get('password', None)
            email = request.GET.get('email', None)
            escuela = request.GET.get('escuela', None)
            direccion = request.GET.get('direccion', None)
            extra = Extras(email=email, escuela=escuela, direccion=direccion)
            user = Usuarios(username=username, password=password)
            extra.save()
            user.save()
        except Exception as e:
            print('Ya existe un Usuario registrado con ese email o username')
            return redirect('services:form_register')

        return redirect('services:index')


class deleteUser(DetailView):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        value = Usuarios.objects.filter(user_id=int(id))
        value.delete()
        print(id)
        return redirect('services:index')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets. ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.


