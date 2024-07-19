from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_login, name='register'),  
    path('about_us/', views.about_us, name='about_us'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('formulario/', views.formulario, name='formulario'),
    path('elements/', views.elements, name='elements'),
    path('contact/', views.contact, name='contact'),
    path('carrito/', views.carrito, name='carrito'),
    path('dibujo/', views.dibujo_list, name='dibujo_list'),
    path('dibujo/<int:pk>/', views.dibujo_detail, name='dibujo_detail'),
    path('dibujo/new/', views.dibujo_new, name='dibujo_new'),
    path('dibujo/<int:pk>/edit/', views.dibujo_edit, name='dibujo_edit'),
    path('dibujo/<int:pk>/delete/', views.dibujo_delete, name='dibujo_delete'),
]
