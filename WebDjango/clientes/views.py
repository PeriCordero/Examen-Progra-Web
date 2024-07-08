
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def index(request):
    context={}
    return render(request, 'pages/index.html', context)
    
def about_us(request):
    context={}
    return render(request, 'pages/about_us.html', context)


def portfolio(request):
    context={}
    return render(request, 'pages/portfolio.html', context)

def portfolio_details(request):
    context={}
    return render(request, 'pages/portfolio_details.html', context)

def formulario(request):
    context={}
    return render(request, 'pages/formulario.html', context)


def elements(request):
    context={}
    return render(request, 'pages/elements.html', context)

def contact(request):
    context={}
    return render(request, 'pages/contact.html', context)

def Carrito(request):
    context={}
    return render(request, 'pages/Carrito.html', context)

def cliente_list(request):
    cliente = Cliente.objects.all()
    return render(request, 'pages/cliente_list.html', {'cliente': cliente})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'pages/cliente_detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'pages/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'pages/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'pages/cliente_confirm_delete.html', {'cliente': cliente})
