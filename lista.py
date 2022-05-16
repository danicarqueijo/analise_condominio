import statistics

leituras = []
media = 0
acima = 0

moradores = int(input('Insira a quantidade de moradores: '))

for i in range(0, moradores):
    leitura = int(input(f'Qual a leitura do {i+1}º morador?: '))

    leituras.append(leitura)
    media = statistics.mean(leituras)

for morador, leitura in enumerate(leituras):
    if leitura > media:
        acima += 1
print(f'Média: {media}\nAcima: {acima}')
