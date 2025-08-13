nome_produto = input("Digite o nome do produto: ")
descricao_produto = input("Digite o descricao do produto: ")
quantidade_produto = float(input("Digite o quantidade comprada do produto: "))
preco = float(input("Digite o preco do produto: "))

total_vendido = quantidade_produto * preco

print(f"O total vendido do {nome_produto} com a descrição {descricao_produto} teve o total de {total_vendido}")
