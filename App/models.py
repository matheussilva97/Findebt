import json
from flask_json import json_response


def listaCliente():
    with open('cliente.json', 'r') as f:
        return json.load(f)


def buscaCliente(cpf):
    jsonArray = listaCliente()
    for jsonObject in jsonArray:
        if jsonObject.get('cpf') == cpf:
            return (jsonObject.get('nome'))

    return json_response(data_="CPF não encontrado")


def atualizaDados(cpf, content):
    jsonArray = listaCliente()
    for jsonObject in jsonArray:
        if jsonObject.get('cpf') == cpf:
            jsonObject['senha'] = content.get('senha')
            jsonObject['status'] = content.get('status')
            with open("login.json", "w") as jsonFile:
                json.dump(jsonObject, jsonFile)
            return json_response(data_="Senha cadastrada com sucesso")

    return json_response(data_="Erro ao cadastrar senha")
