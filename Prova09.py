# Criar dicionario para armazenar nome e preço de cinco produtos e exibir valor total 

#armazenar
produtos = {}

#inserir produto e valor
for i in range(5):
    nome_do_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_do_produto = float(input(f"Digite o preço de {nome_do_produto}: "))
    produtos[nome_do_produto] = preco_do_produto

#exibir produtos e preços cadastrados
print("\nProdutos e preços cadastrados: ")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

#exibir valor total
valor_total = sum(produtos.values())
print(f"\nValor total da compra: R${valor_total:.2f}")