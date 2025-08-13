nulo = int(input("Digite os votos nulos: "))
brancos = int(input("Digite os votos brancos: "))
validos = int(input("Digite os votos validos: "))

totaleleitores = nulo + brancos + validos

percbranco = (brancos * 100)/ totaleleitores
percnulo = (nulo * 100)/ totaleleitores
validos = (validos * 100)/ totaleleitores

print(f"O total dos votos é de: {totaleleitores}")
print(f"O percentual de votos em Branco é de: {percbranco}")
print(f"O percentual de votos nulos é de: {percnulo}")
print(f" O percentual de votos validos é de: {validos}")
