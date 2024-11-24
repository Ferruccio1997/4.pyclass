from typing import Dict
import json


produto_1: dict[str, int, float, bool] = {
    'nome': 'sapato',
    'quantidade': 39,
    'preco': 10.38,
    'disponibilidade': True
}

produto_2: dict[str, int, float, bool] = {
    'nome': 'televisao',
    'quantidade': 10,
    'preco': 70.38,
    'disponibilidade': False
}

carrinho: list[dict] = []

carrinho.append(produto_1)
carrinho.append(produto_2)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)