from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio_details', views.portfolio_details, name='portfolio_details'),
    path('formulario', views.formulario, name='formulario'),
    path('elements', views.elements, name='elements'),
    path('contact', views.contact, name='contact'),
    path('Carrito', views.Carrito, name='Carrito'),
    path('cliente_list', views.cliente_list, name='cliente_list'),
    path('<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('new/', views.cliente_create, name='cliente_create'),
    path('<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]

    