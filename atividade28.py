# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

produtos = []
estoques = []

for i in range(5):
    produto = str(input("digite os produtos: "))
    estoque = int(input("digite a quantidade de produtos em estoque: "))
    produtos.append(produto)
    estoques.append(estoque)

print("\nprodutos com estoque zerado; ")
for i in range(5):
    if estoques[i] == 0:
        print(produtos [i])

