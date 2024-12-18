from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Backup

# Obtendo o modelo de usuário personalizado
Usuario = get_user_model()

# Helper para verificar se o usuário é Admin
def is_admin(user):
    return user.is_staff

# Usuários
@login_required
@user_passes_test(is_admin)
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'adminas/usuarios.html', {'usuarios': usuarios})

# Função de vista para adicionar usuários
@login_required
def adicionar_usuarios(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')  # Redireciona para a lista de usuários ou outra página
    else:
        form = UserCreationForm()

    return render(request, 'adminas/adicionar_usuarios.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def editar_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    if request.method == 'POST':
        usuario.is_active = 'ativar' in request.POST
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'adminas/editar_usuario.html', {'usuario': usuario})

# Função de vista para desativar usuários
@login_required
def desativar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.is_active = False
    usuario.save()
    return redirect('usuarios')  # Redireciona para a lista de usuários ou outra página

@login_required
@user_passes_test(is_admin)
def resetar_senha(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    if request.method == 'POST':
        nova_senha = request.POST.get('nova_senha')
        if nova_senha:
            usuario.set_password(nova_senha)
            usuario.save()
            return redirect('listar_usuarios')
    return render(request, 'adminas/resetar_senha.html', {'usuario': usuario})

# Permissões
@login_required
@user_passes_test(is_admin)
def listar_permissoes(request):
    grupos = Group.objects.all()
    permissoes = Permission.objects.all()
    return render(request, 'adminas/permissoes.html', {'grupos': grupos, 'permissoes': permissoes})

@login_required
@user_passes_test(is_admin)
def configurar_permissao(request):
    if request.method == 'POST':
        # Lógica de configuração de permissões
        pass
    return render(request, 'adminas/configurar_permissao.html')

# Backups
@login_required
@user_passes_test(is_admin)
def listar_backups(request):
    backups = Backup.objects.all()
    return render(request, 'adminas/backups.html', {'backups': backups})

@login_required
@user_passes_test(is_admin)
def criar_backup(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        Backup.objects.create(type=tipo, file_path='caminho_a_definir')
        return redirect('listar_backups')
    return render(request, 'adminas/criar_backup.html')

@login_required
@user_passes_test(is_admin)
def verificar_atualizacoes(request):
    # Lógica para verificar atualizações
    atualizacao_pendente = False  # Exemplo
    return render(request, 'adminas/verificar_atualizacoes.html', {'atualizacao_pendente': atualizacao_pendente})
