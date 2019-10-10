from django.urls import path
from services import views

namespace = 'services'
urlpatterns = [
    path('index/', views.indexView.as_view(), name='index'),
    path('register/', views.registerView.as_view(), name='form_register'),
    path('register/add', views.addUser.as_view(), name='add'),
    path('register/delete/<id: int>', views.addUser.as_view(), name='delete'),
]

