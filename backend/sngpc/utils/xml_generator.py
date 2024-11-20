from lxml import etree
from datetime import datetime

def gerar_xml(config, movimentacoes):
    """
    Gera o XML para envio ao SNGPC.
    """
    root = etree.Element("MensagemSNGPC")
    
    # Configurações básicas
    cabecalho = etree.SubElement(root, "Cabecalho")
    etree.SubElement(cabecalho, "CNPJ").text = config.cnpj
    etree.SubElement(cabecalho, "RazaoSocial").text = config.nome_farmacia
    etree.SubElement(cabecalho, "DataInicio").text = datetime.now().strftime("%Y-%m-%d")
    etree.SubElement(cabecalho, "DataFim").text = datetime.now().strftime("%Y-%m-%d")

    # Movimentações
    corpo = etree.SubElement(root, "Corpo")
    movimentacoes_element = etree.SubElement(corpo, "Movimentacoes")

    for mov in movimentacoes:
        movimentacao = etree.SubElement(movimentacoes_element, "Movimentacao")
        etree.SubElement(movimentacao, "Tipo").text = mov.tipo_movimentacao
        etree.SubElement(movimentacao, "Medicamento").text = mov.medicamento
        etree.SubElement(movimentacao, "Quantidade").text = str(mov.quantidade)
        etree.SubElement(movimentacao, "Data").text = mov.data_movimentacao.strftime("%Y-%m-%d")

    return etree.tostring(
        root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
    )
