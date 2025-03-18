totala = 0
totalb = 0
totalc = 0
totalcan = 0
a = 10
b = 20
c = 30
lista = []
for i in range(4):
 candidato = int(input('digite seu voto (10, 20, 30)= '))
 if candidato == a:
  totala += 1
  totalcan += 1
 elif candidato == b:
  totalb += 1
  totalcan += 1
 elif candidato == c:
  totalc += 1
  totalcan += 1
 else:
  print('voto invalido')
print(f'total de votos do candidato A: {totala}')
print(f'total de votos do candidato B: {totalb}')
print(f'total de votos do candidato C: {totalc}')
print(f'total de votos: {totalcan}')