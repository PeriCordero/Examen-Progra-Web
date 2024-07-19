from django.shortcuts import render, get_object_or_404, redirect
from .models import Dibujo
from .forms import DibujoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def user_login(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST' and 'login' in request.POST:
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('index')  # Redirect to a success page or dashboard

    if request.method == 'POST' and 'register' in request.POST:
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            auth_login(request, user)
            return redirect('index')  # Redirect to a success page or dashboard

    return render(request, 'pages/login.html', {'login_form': login_form, 'register_form': register_form})



def about_us(request):
    context = {}
    return render(request, 'pages/about_us.html', context)

def portfolio(request):
    context = {}
    return render(request, 'pages/portfolio.html', context)

def portfolio_details(request):
    context = {}
    return render(request, 'pages/portfolio_details.html', context)

def formulario(request):
    context = {}
    return render(request, 'pages/formulario.html', context)

def elements(request):
    context = {}
    return render(request, 'pages/elements.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def carrito(request):
    context = {}
    return render(request, 'pages/carrito.html', context)

@login_required
def dibujo_list(request):
    dibujos = Dibujo.objects.all()
    return render(request, 'pages/dibujo_list.html', {'dibujos': dibujos})

@login_required
def dibujo_detail(request, pk):
    dibujo = get_object_or_404(Dibujo, pk=pk)
    return render(request, 'pages/dibujo_detail.html', {'dibujo': dibujo})

@login_required
def dibujo_new(request):
    if request.method == "POST":
        form = DibujoForm(request.POST)
        if form.is_valid():
            dibujo = form.save()
            return redirect('dibujo_detail', pk=dibujo.pk)
    else:
        form = DibujoForm()
    return render(request, 'pages/dibujo_edit.html', {'form': form})

@login_required
def dibujo_edit(request, pk):
    dibujo = get_object_or_404(Dibujo, pk=pk)
    if request.method == "POST":
        form = DibujoForm(request.POST, instance=dibujo)
        if form.is_valid():
            dibujo = form.save()
            return redirect('dibujo_detail', pk=dibujo.pk)
    else:
        form = DibujoForm(instance=dibujo)
    return render(request, 'pages/dibujo_edit.html', {'form': form})

@login_required
def dibujo_delete(request, pk):
    dibujo = get_object_or_404(Dibujo, pk=pk)
    dibujo.delete()
    return redirect('dibujo_list')


