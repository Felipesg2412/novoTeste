numero = int(input('digite um numero = '))
if numero< 2:
 print('Não é primo')
else:
 for i in range(2,numero):
  if numero%i== 0:
   print('não é primo: ')
   break
 else:
  print('é primo')
