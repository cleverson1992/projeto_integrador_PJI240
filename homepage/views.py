from django.shortcuts import redirect, render
# from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from .models import Localidades, DadosProdutos


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        nome_filtrar = request.GET.get('nome_filtrar')

        if nome_filtrar:
            dadosprodutos = DadosProdutos.objects.filter(produto__icontains=nome_filtrar)
        else:
            dadosprodutos = DadosProdutos.objects.all()

        return render(request, 'homepage.html', {'dadosprodutos': dadosprodutos})
    
    else:
        return redirect('/usuarios/login')
        

def cadastro_estoque(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            localidades = Localidades.objects.all()
            return render(request, 'cadastro_estoque.html', {'localidades': localidades})
        else:
            return redirect('/usuarios/login')
    elif request.method == "POST":
        produto = request.POST.get('produto')
        modelo = request.POST.get('modelo')
        localidade = request.POST.get('localidade')
        quantidade = request.POST.get('quantidade')

        dados_produtos = DadosProdutos(
            produto=produto,
            modelo=modelo,
            localidade_id=localidade,
            quantidade=quantidade,
            user=request.user,
        )

        dados_produtos.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado!')
        return redirect('/cadastro_estoque/')
    
    
def gerenciar_estoque(request):
    if request.user.is_authenticated:
        nome_filtrar = request.GET.get('nome_filtrar')

        if nome_filtrar:
            dadosprodutos = DadosProdutos.objects.filter(produto__icontains=nome_filtrar)
        else:
            dadosprodutos = DadosProdutos.objects.all()

        return render(request, 'gerenciar_estoque.html', {'dadosprodutos': dadosprodutos})

    else:
        return redirect('/usuarios/login')


def deletar(request, id):
    produto = DadosProdutos.objects.get(id=id)

    produto.delete()

    return redirect('/gerenciar_estoque/')
