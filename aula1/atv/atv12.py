azulejo_altura = float(input("Digite o altura do azulejos: "))
azulejo_largura = float(input("Digite o largura do azulejos: "))
a_p = float(input("Digite a altura da parede: "))
l_p = float(input("Digite a largura da parede: "))

area_parede = l_p * a_p
area_azulejos = azulejo_altura * azulejo_largura

azulejos_necessarios = area_parede / area_azulejos

print(f"O total necessario de azulejos é de: {azulejos_necessarios}")
