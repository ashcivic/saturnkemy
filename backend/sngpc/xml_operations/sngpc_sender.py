from zeep import Client
from zeep.transports import Transport
import requests
from lxml import etree
from backend.sngpc.utils import get_ambiente_url

def enviar_xml_sngpc(xml_path):
    wsdl_url = get_ambiente_url() 
    with open(xml_path, "r", encoding="utf-8") as file:
        xml_data = file.read()

    try:
        transport = Transport(session=requests.Session())
        client = Client(wsdl=wsdl_url, transport=transport)
        response = client.service.EnviarInventario(xml_data)  # Substitua com o método correto
        return response
    except Exception as e:
        return f"Erro no envio: {str(e)}"

def processar_mensagens_retorno(xml_retorno):
    # Carregar o schema
    schema_path = "caminho/para/sngpcRetorno.xsd"
    schema = etree.XMLSchema(file=schema_path)

    # Validar XML
    parser = etree.XMLParser(schema=schema)
    try:
        tree = etree.fromstring(xml_retorno, parser)
        mensagens = tree.xpath("//mensagem/text()")  # Ajuste baseado no XML real
        return True, mensagens
    except etree.XMLSyntaxError as e:
        return False, [str(e)]