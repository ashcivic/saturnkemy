import xml.etree.ElementTree as ET
import base64
import hashlib
import zipfile
from io import BytesIO

def gerar_xml_inventario(inventario):
    root = ET.Element("mensagemSNGPCInventario")
    cabecalho = ET.SubElement(root, "cabecalho")
    ET.SubElement(cabecalho, "cnpjEmissor").text = inventario.cnpj_emissor
    ET.SubElement(cabecalho, "cpfTransmissor").text = inventario.cpf_transmissor
    ET.SubElement(cabecalho, "data").text = str(inventario.data)

    corpo = ET.SubElement(root, "corpo")
    medicamentos = ET.SubElement(corpo, "medicamentos")

    for medicamento in inventario.medicamentos.all():
        entrada = ET.SubElement(medicamentos, "entradaMedicamentos")
        ET.SubElement(entrada, "classeTerapeutica").text = str(medicamento.classe_terapeutica)
        ET.SubElement(entrada, "registroMSMedicamento").text = medicamento.registro_ms
        ET.SubElement(entrada, "numeroLoteMedicamento").text = medicamento.numero_lote
        ET.SubElement(entrada, "quantidadeMedicamento").text = str(medicamento.quantidade)
        ET.SubElement(entrada, "unidadeMedidaMedicamento").text = str(medicamento.unidade_medida)

    xml_str = ET.tostring(root, encoding='iso-8859-1', xml_declaration=True)
    return xml_str

def compactar_e_converter_base64(xml_str):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("inventario.xml", xml_str)
    buffer.seek(0)
    base64_str = base64.b64encode(buffer.read()).decode('utf-8')
    return base64_str

def calcular_md5(base64_str):
    md5 = hashlib.md5(base64_str.encode('utf-8')).hexdigest()
    return md5
