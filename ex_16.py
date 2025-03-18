totalp = 15
q = 0
t = 0
c = 0
u = 0
s = 0
for i in range (15):
 idade = int(input('digite a sua idade: '))
 if idade <= 15:
  q += 1
 elif idade >15 and idade <=30:
  t += 1
 elif idade >30 and idade <=45:
  c += 1
 elif idade >45 and idade <=60:
  u += 1
 elif idade >=61:
  s += 1
print(f'Quantidade de pessoas de até 15 anos: {q}')
print(f'Quantidade de pessoas de até 60 anos: {t}')
print(f'Quantidade de pessoas de até 45 anos: {c}')
print(f'Quantidade de pessoas de até 60 anos: {u}')
print(f'Quantidade de pessoas com mais de 61 anos: {s}')
print(f'Porcentagem da primeira e ultima faixa estaria com relção ao total é: {((q+s)/totalp)*100}%')