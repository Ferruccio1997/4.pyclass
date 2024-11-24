produto_1: str = 'sapato'
produto_2: str = 'camiseta'
produto_3: str = 'videogame'

produtos: list = []

produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop() # retira o ultimo adicionado
#produtos.remove(produto_1) # remove o indicado

print(produtos)

numeros = []
numeros.extend(range(0,5))
print(numeros)