from django.test import TestCase, Client
from django.urls import reverse
from .models import Produto, ConfiguracaoSngpc



class SNGPCTestCase(TestCase):
    def setUp(self):
        # Criar dados de teste
        Produto.objects.create(
            nome="Dipirona 500mg",
            codigo_barras="7891234567890",
            registro_ms="123456789",
            lote="L1234",
            quantidade=100
        )

    def test_buscar_produto(self):
        produto = Produto.objects.get(codigo_barras="7891234567890")
        self.assertEqual(produto.nome, "Dipirona 500mg")

    def test_processar_xml_view_autenticacao(self):
        client = Client()
        response = client.get(reverse("sngpc_processar"))
        self.assertEqual(response.status_code, 302)  # Redireciona para login


class AmbienteTestCase(TestCase):
    def setUp(self):
        ConfiguracaoSngpc.objects.create(ambiente="homologacao")

    def test_ambiente_homologacao(self):
        configuracao = ConfiguracaoSngpc.objects.first()
        self.assertEqual(configuracao.ambiente, "homologacao")