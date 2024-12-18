from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from .models import Grupo, Backup, GroupPermission, UserPermission, DadosEmpresa
from django.urls import path
from django.shortcuts import render, redirect
from .forms import DadosEmpresaForm
from .utils import buscar_dados_cnpj 

# Obtendo o modelo de usuário personalizado
Usuario = get_user_model()

#@admin.register(Usuario)
#class UsuarioAdmin(admin.ModelAdmin):
#   list_display = ('username', 'email', 'is_active', 'created_at', 'updated_at')
#    list_filter = ('is_active',)
#    search_fields = ('username', 'email')

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ('type', 'created_at', 'file_path')
    list_filter = ('type',)
    search_fields = ('file_path',)

@admin.register(GroupPermission)
class GroupPermissionAdmin(admin.ModelAdmin):
    list_display = ('group', 'app_label', 'codename')
    search_fields = ('group__name', 'app_label', 'codename')

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'app_label', 'codename')
    search_fields = ('user__username', 'app_label', 'codename')

@admin.register(DadosEmpresa)
class DadosEmpresaAdmin(admin.ModelAdmin):
    list_display = ("razao_social", "cnpj", "telefone", "email")
    search_fields = ("cnpj", "razao_social", "nome_fantasia")
    actions = None

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("importar-cnpj/", self.importar_cnpj_view, name="importar_cnpj"),
        ]
        return custom_urls + urls

    def importar_cnpj_view(self, request):
        if request.method == "POST":
            cnpj = request.POST.get("cnpj")
            try:
                dados = buscar_dados_cnpj(cnpj)  # Busca os dados pela API
                form = DadosEmpresaForm(dados)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Empresa cadastrada com sucesso!")
                    return redirect("admin:adminas_dadosempresa_changelist")
                else:
                    messages.error(request, "Erro ao validar os dados.")
            except Exception as e:
                messages.error(request, f"Erro ao buscar os dados: {e}")

        return render(request, "adminas/importar_cnpj.html")

