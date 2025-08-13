salario = float(input("Digite o salario "))
reajuste = float(input("Digite o reajuste "))
aumento = (reajuste * salario) /100
salario_final = aumento + salario

print(f"O salário final é de: {salario_final}")
