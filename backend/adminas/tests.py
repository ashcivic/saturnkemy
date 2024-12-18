from django.test import TestCase
from .models import Usuario, Grupo, Backup

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(username="admin", email="admin@example.com", ativo=True)

    def test_usuario_creation(self):
        usuario = Usuario.objects.get(username="admin")
        self.assertEqual(usuario.email, "admin@example.com")
        self.assertTrue(usuario.ativo)

class GrupoTestCase(TestCase):
    def setUp(self):
        Grupo.objects.create(name="Administradores", descricao="Grupo com acesso total")

    def test_grupo_creation(self):
        grupo = Grupo.objects.get(name="Administradores")
        self.assertEqual(grupo.descricao, "Grupo com acesso total")

class BackupTestCase(TestCase):
    def setUp(self):
        Backup.objects.create(tipo="Parcial", completo=False)

    def test_backup_creation(self):
        backup = Backup.objects.get(tipo="Parcial")
        self.assertFalse(backup.completo)
