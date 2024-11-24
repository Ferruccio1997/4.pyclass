# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# lista: list[int] = []
# lista.extend(range(1,11))

# for num in lista:
#     print(num**2)



# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# lista: list[str] = ["Python", "Java", "C++", "JavaScript"]

# lista.remove('C++')
# lista.append('Ruby')

# print(lista)



# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# dicionario: dict[str, str, int] = {
#     'titulo': 'Hobbit',
#     'autor': 'J. R. R. Tolkien',
#     'ano de publicacao': 1937
# }

# print(dicionario)



# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# string: str = 'O livro do hobbit e muito bom'
# lista_string: list = list(string.lower())
# dicionario: dict = {}

# for item in lista_string:
#     if item in dicionario:
#         dicionario[item] += 1
#     else:
#         dicionario[item] = 1

# print(dicionario)



# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# lista_compra: list[str] = ['maça', 'banana', 'cereja']
# preco: dict[float] = {
#     'maça': 0.45,
#     'banana': 0.3,
#     'cereja': 0.65
# }

# preco_total: float = 0

# try:
#     for item in lista_compra:
#         preco_total = preco_total + preco[item]

#     print(preco_total)
# except KeyError:
#     print('Erro de chave!')



# 6. Eliminação de Duplicatas: Objetivo: Dada uma lista de emails, remover todos os duplicados.
# lista_emails: list[str] = ['ferruccio@gmai.com', 'luana@gmai.com', 'ferruccio@gmai.com']

# lista_emails_unique = set(lista_emails)

# print(lista_emails_unique)



# 7. Filtragem de Dados: Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# lista_idade: list[int] = [18, 24, 60, 8, 10, 16]

# lista_idade_filtrado = [idade for idade in lista_idade if idade >= 18 ]

# print(lista_idade_filtrado)



# 8. Ordenação Personalizada: Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# dicionarios_pessoas: list[dict] = [
#     {'nome': 'Ferruccio'},
#     {'nome': 'Luana'},
#     {'nome': 'Cecilia'},
#     {'nome': 'Gordon'}
# ]

# sorted_list = sorted(dicionarios_pessoas, key=lambda x: x['nome'])

# print(sorted_list)



# 9. Agregação de Dados: Objetivo: Dado um conjunto de números, calcular a média.
# lista_numeros: list[int] = [2,4,5,7,10]

# media = sum(lista_numeros) / len(lista_numeros)

# print(media)



# 10. Divisão de Dados em Grupos: Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# lista_numeros: list[int] = [1,2,3,4,5,6,7,8]

# lista_par: list[int] = [item for item in lista_numeros if item%2 == 0]
# lista_inpar: list[int] = [item for item in lista_numeros if item%2 != 0]

# print(lista_par)
# print(lista_inpar)



# 11. Atualização de Dados: Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# lista_produtos: list[dict] = [
#     {'produto': 'tv', 'preco': 1000},
#     {'produto': 'celular', 'preco': 500},
#     {'produto': 'tablet', 'preco': 700}
# ]

# preco_novo: dict[str, int] = {
#     'produto': 'celular', 'preco': 600
# }

# for item in lista_produtos:
#     if item['produto'] == preco_novo['produto']:
#         item['preco'] = preco_novo['preco']

# print(lista_produtos)



# 12. Fusão de Dicionários: Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
# produto: dict[str, int] = {'produto': 'tv', 'preco': 1000}
# novas_infos: dict[str, int] = {'fabricante': 'rairey', 'ano': 1990}

# produto.update(novas_infos)

# print(produto)



# 13. Filtragem de Dados em Dicionário: Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# estoque: list[dict] = [
#     {'nome': 'celular', 'quantidade': 100},
#     {'nome': 'tv', 'quantidade': 0},
#     {'nome': 'tablet', 'quantidade': 60}
# ]

# estoque_filtrado = [item for item in estoque if item['quantidade'] > 0]

# print(estoque_filtrado)



# 14. Extração de Chaves e Valores: Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
# dicinario: dict[str] = {
#     'livro.1': 'Hobbit',
#     'livro.2': 'Senhor dos Aneis 1',
#     'livro.3': 'Senhor dos Aneis 2'
# }

# keys = list(dicinario.keys())
# values = list(dicinario.values())

# print(keys)
# print(values)



# 15. Contagem de Frequência de Itens: Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
# string: str = 'O livro do hobbit e muito bom'

# lista_string: list[str] = list(string.lower())

# contagem: dict[str, int] = {}

# for item in lista_string:
#     if item in contagem:
#         contagem[item] += 1
#     else:
#         contagem[item] = 1

# print(contagem)



# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# def soma_lista(lista: list) -> int:
#     resultado = 0
#     for num in lista:
#         resultado = resultado + num
#     return resultado

# lista: list[int] = [1,2,3,4,5,6,7,8]
# print(soma_lista(lista))



# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# def teste_primo(numero: int) -> bool:
#     lista_factor = []

#     for i in range(1, numero+1):
#         if numero % i == 0:
#             lista_factor.append(i)
    
#     if len(lista_factor) == 2:
#         return True
#     else:
#         return False
    
# print(teste_primo(4))



# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# def inverte_string(string: str) -> str:
#     nova_string = string[::-1]

#     return nova_string

# print(inverte_string('Ouviram'))



# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# def combinacao_soma_numero(lista: list, numero: int) -> list:
#     lista_combinacao = []
#     for i in range(len(lista)):
#         for j in range(len(lista)):
#             if i != j and lista[i] + lista[j] == numero:
#                 lista_combinacao.append([lista[i], lista[j]])

#     return lista_combinacao

# print(combinacao_soma_numero([1,2,3,4,5,6,7,8], 7))



# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
# def ordered_keys(dicionario: dict) -> list:
#     lista_keys = list(dicionario.keys())
#     lista_keys.sort()

#     return lista_keys

# dicionario = {
#     'nome': 'Ferruccio',
#     'idade': 18,
#     'altura': 190
# }

# print(ordered_keys(dicionario))