from .models import ConfiguracaoSngpc

def get_ambiente_url():
    configuracao = ConfiguracaoSngpc.objects.first()  # Retorna a configuração atual
    if configuracao and configuracao.ambiente == "producao":
        return "https://sngpc.anvisa.gov.br/webservice/sngpc.wsdl"  # Produção
    return "https://homologacao.anvisa.gov.br/webservice/sngpc.wsdl"  # Homologação
