import requests

def enviar_xml(xml, ambiente):
    """
    Envia o XML para o endpoint correto baseado no ambiente.
    """
    endpoints = {
        "homologacao": "https://homologacao.anvisa.gov.br/sngpc",
        "producao": "https://producao.anvisa.gov.br/sngpc",
    }

    url = endpoints.get(ambiente)
    if not url:
        raise ValueError("Ambiente inválido.")

    headers = {"Content-Type": "application/xml"}
    response = requests.post(url, data=xml, headers=headers)

    return response.status_code, response.text
