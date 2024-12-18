from lxml import etree
import os
from backend.sngpc.models import XML
from backend.adminas.models import DadosEmpresa


def gerar_xml_sngpc(dados_cabecalho, medicamentos, insumos):
    from adminas.models import DadosEmpresa

    # Buscar os dados da empresa
    dados_empresa = DadosEmpresa.objects.first()
    if not dados_empresa:
        raise Exception("Dados da empresa não cadastrados. Cadastre as informações antes de gerar o XML.")

    # Adicionar os dados da empresa ao cabeçalho
    dados_cabecalho["cnpjEmissor"] = dados_empresa.cnpj
    dados_cabecalho["cpfTransmissor"] = "72586648153"  # Exemplo, ajuste conforme necessário
    dados_cabecalho["data"] = "2024-06-10"  # Atualize para a data dinâmica se necessário

    # Restante do código permanece o mesmo
    ns = "urn:sngpc-schema"
    nsmap = {None: ns}
    root = etree.Element("mensagemSNGPCInventario", nsmap=nsmap)

    # Cabeçalho
    cabecalho = etree.SubElement(root, "cabecalho")
    for tag, value in dados_cabecalho.items():
        etree.SubElement(cabecalho, tag).text = value

    # Corpo
    corpo = etree.SubElement(root, "corpo")

    # Medicamentos
    meds = etree.SubElement(corpo, "medicamentos")
    for med in medicamentos:
        entrada = etree.SubElement(meds, "entradaMedicamentos")
        med_ent = etree.SubElement(entrada, "medicamentoEntrada")
        for tag, value in med.items():
            etree.SubElement(med_ent, tag).text = value

    # Insumos
    ins = etree.SubElement(corpo, "insumos")
    for insumo in insumos:
        entrada = etree.SubElement(ins, "entradaInsumos")
        insumo_ent = etree.SubElement(entrada, "insumoEntrada")
        for tag, value in insumo.items():
            etree.SubElement(insumo_ent, tag).text = value

    # Salva o arquivo XML
    path = os.path.join("sngpc", "xml_operations", "sngpc_inventario.xml")
    tree = etree.ElementTree(root)
    tree.write(path, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    # Salva no banco de dados
    xml_record = XML(nome="sngpc/sngpc_inventario.xml", arquivo=path)
    xml_record.save()
    return path