desconto = 0
valor_final = 0

print("Tabela de descontos da loja:")
print()
print("Valor da Compra - Porcentagem de Desconto - Valor Final de sua Compra")
print()

for compra in range (500,3100,100):
            desconto = (compra - 500) / 100 + 1
            valor_final = compra - (compra * (desconto/100))
            if desconto > 25:
                    desconto = 25
            else:
                print(f"   {compra}   -  {desconto}%   -   {valor_final}")