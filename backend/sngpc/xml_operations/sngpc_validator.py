import xmlschema
import os

def validar_xml(xml_path):
    xsd_path = os.path.join("sngpc", "xml_operations", "schemas", "sngpcSimpleTypes.xsd")
    schema = xmlschema.XMLSchema(xsd_path)
    try:
        schema.validate(xml_path)
        return True, "XML válido!"
    except xmlschema.XMLSchemaValidationError as e:
        return False, str(e)
