from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    ocupacion = forms.CharField(label='ocupacion', max_length=100)
    edad = forms.CharField(label='edad', max_length=100)
    escuela = forms.CharField(label='escuela', max_length=100)
    direccion = forms.CharField(label='direccion', max_length=100)
    actividades = forms.CharField(label='actividades', max_length=100)