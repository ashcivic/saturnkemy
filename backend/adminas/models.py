from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Modelo de Usuário
class DadosEmpresa(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    inscricao_municipal = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cep = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    porte = models.CharField(max_length=50, blank=True, null=True)
    abertura = models.DateField(blank=True, null=True)
    atividade_principal = models.CharField(max_length=255, blank=True, null=True)
    natureza_juridica = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    situacao = models.CharField(max_length=50, blank=True, null=True)
    data_situacao = models.DateField(blank=True, null=True)
    motivo_situacao = models.CharField(max_length=255, blank=True, null=True)
    situacao_especial = models.CharField(max_length=255, blank=True, null=True)
    data_situacao_especial = models.DateField(blank=True, null=True)
    capital_social = models.CharField(max_length=50, blank=True, null=True)
    simples_optante = models.BooleanField(default=False)
    simei_optante = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_fantasia
    
# Modelo de Usuário
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255) 

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'Os grupos aos quais este usuário pertence.'
        ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_(
            'As permissões específicas para este usuário.'
        ),
    )

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return self.username

# Modelo de Grupos Personalizados
class Grupo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Grupo')
        verbose_name_plural = _('Grupos')

    def __str__(self):
        return self.nome

# Permissões para Usuários
class UserPermission(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='custom_permissions'
    )
    app_label = models.CharField(max_length=50, help_text="Nome do app para o qual a permissão é concedida.")
    codename = models.CharField(max_length=100, help_text="Codename da permissão específica.")

    class Meta:
        unique_together = ('user', 'app_label', 'codename')
        verbose_name = _('Permissão de Usuário')
        verbose_name_plural = _('Permissões de Usuários')

    def __str__(self):
        return f"{self.user.username}: {self.app_label} - {self.codename}"

# Permissões para Grupos
class GroupPermission(models.Model):
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        related_name='custom_group_permissions'
    )
    app_label = models.CharField(max_length=50, help_text="Nome do app para o qual a permissão é concedida.")
    codename = models.CharField(max_length=100, help_text="Codename da permissão específica.")

    class Meta:
        unique_together = ('group', 'app_label', 'codename')
        verbose_name = _('Permissão de Grupo')
        verbose_name_plural = _('Permissões de Grupos')

    def __str__(self):
        return f"{self.group.name}: {self.app_label} - {self.codename}"

# Backups
class Backup(models.Model):
    BACKUP_TYPES = [
        ('partial', _('Parcial')),
        ('full', _('Total')),
        ('scheduled', _('Periódico')),
    ]

    type = models.CharField(max_length=10, choices=BACKUP_TYPES, default='full', verbose_name=_('Tipo de Backup'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de Criação'))
    file_path = models.CharField(max_length=255, verbose_name=_('Caminho do Arquivo'))

    class Meta:
        verbose_name = _('Backup')
        verbose_name_plural = _('Backups')

    def __str__(self):
        return f"{self.get_type_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

# Atualizações do Sistema
class SystemUpdate(models.Model):
    version = models.CharField(max_length=50, verbose_name=_('Versão'))
    release_date = models.DateField(verbose_name=_('Data de Lançamento'))
    applied = models.BooleanField(default=False, verbose_name=_('Aplicada'))

    class Meta:
        verbose_name = _('Atualização do Sistema')
        verbose_name_plural = _('Atualizações do Sistema')

    def __str__(self):
        return f"Versão {self.version} - {'Aplicada' if self.applied else 'Pendente'}"
