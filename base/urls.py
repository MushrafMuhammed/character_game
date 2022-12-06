from django.urls import path,include
from . import views

urlpatterns = [
    path('baseground', views.basegroundfun, name='baseground'),
    

]