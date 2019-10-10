from django.urls import path, include
from services import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
namespace = 'services'
urlpatterns = [
    path('index/', views.indexView.as_view(), name='index'),
    path('register/', views.registerView.as_view(), name='form_register'),
    path('register/add', views.addUser.as_view(), name='add'),
    path('register/delete/<int:id>', views.deleteUser.as_view(), name='delete'),
    path('', include(router.urls)),

]

