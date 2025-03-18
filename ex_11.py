soma = 0
for i in range (5):
 idade = int(input('digite a sua idade = '))
 soma += idade
media = soma/5
if media <= 25:
 print(f'turma jovem {media}')
elif media <= 60:
 print(f'turma adulta {media}')
else:
 print(f'turma idosa {media}')