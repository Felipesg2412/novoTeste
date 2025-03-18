soma = 0
b = 54000

for i in range(5):
 cliente = float(input('digite o valor da conta = '))
 soma += cliente
 
 if soma > b:
   print(f'o valor foi superado em {soma - b} ')
 else:
   print(f'valor não foi superado')