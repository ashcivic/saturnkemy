import requests
import xml.etree.ElementTree as ET

class SNGPCService:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.base_url = self.get_base_url()

    def get_base_url(self):
        """Define a URL base dependendo do ambiente."""
        if self.ambiente == 'producao':
            return 'https://sngpc.anvisa.gov.br/producao'
        return 'https://sngpc.anvisa.gov.br/homologacao'

    def gerar_xml(self, dados):
        """Gera um XML conforme o padrão do SNGPC."""
        root = ET.Element('SNGPC')
        for chave, valor in dados.items():
            ET.SubElement(root, chave).text = str(valor)
        return ET.tostring(root, encoding='utf-8')

    def enviar_xml(self, xml_data):
        """Envia o XML gerado para o SNGPC."""
        headers = {'Content-Type': 'application/xml'}
        url = f"{self.base_url}/enviar"
        response = requests.post(url, data=xml_data, headers=headers)
        return response.status_code, response.content
