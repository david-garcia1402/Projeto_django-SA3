from django.shortcuts import render, redirect
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tela apra o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.id = request.POST.get('id_usuario')
    novo_usuario.save()
    #Exibir todos os usuários já cadastrados em uma nova pagina.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html',usuarios)

def editar(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    return render(request, "usuarios/editar.html", {"usuario":usuario})

def update(request, id):
    usuarioNovo = Usuario()
    novo_nome = request.GET.get('nome')
    nova_idade = request.GET.get('idade')

    usuarioNovo.nome = novo_nome
    usuarioNovo.idade = nova_idade
    usuarioNovo.save()

    usuarioNovo.save()
    return redirect(home)

def regras(request):
    return render(request, 'usuarios/regras.html')