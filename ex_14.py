for i in range(1,999):
 nota = float(input('Digite sua nota:'))
 if nota < 0:
  print('valor invalido')
 elif nota > 10:
  print('valor invalido')
 else:
  print('valor valido')
  break