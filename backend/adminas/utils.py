import requests

def buscar_dados_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj.replace('.', '').replace('/', '').replace('-', '')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "status" in data and data["status"] == "ERROR":
            raise Exception(data["message"])

        return {
            "cnpj": cnpj,
            "razao_social": data.get("nome"),
            "nome_fantasia": data.get("fantasia"),
            "endereco": f"{data.get('logradouro')}, {data.get('numero')} - {data.get('bairro')}, {data.get('municipio')}/{data.get('uf')} CEP {data.get('cep')}",
            "telefone": data.get("telefone"),
            "email": data.get("email"),
            "inscricao_estadual": data.get("atividade_principal")[0].get("code") if data.get("atividade_principal") else None,
        }
    else:
        raise Exception("Erro ao conectar à API.")
