#Autor: Cristian Balsanelli
# Linguagem: Python
# Programa que calcula o valor a ser pago após o desconto de acordo com o valor da compra.

#Entrada de dados
valorCompra = float(input("Insira o valor total da compra: ")) #valor digitado pelo usuário 
#é transformado em tipo float para permitir casas decimais e armazenado na variavel valorCompra

#Processamento e saída de dados de acordo com o valor da compra
if valorCompra < 200.00:
 # se o valor da compra for menor que 200.00, aplica-se um desconto de 5%
    print("Voce recebeu um desconto de 5%") #imprime a mensagem "Voce recebeu um desconto de 5%"            
    valorDesconto = valorCompra * 0.95  # calcula o valor a ser pago após o desconto de 5% e 
    # armazena na variavel valorDesconto
    print("O valor a ser pago após o desconto é: R$", f"{valorDesconto:.2f}")
    # imprime na tela o valor a ser pago após o desconto, formatado com duas casas decimais
elif valorCompra >= 200.00 and valorCompra < 300.00:
 # se o valor da compra for maior ou igual a 200 e menor que 300, entra neste bloco 
    print("Voce recebeu um desconto de 10%") #imprime a mensagem "Voce recebeu um desconto de 10%" 
    valorDesconto = valorCompra * 0.90 # calcula o valor a ser pago após o desconto de 10% e 
    # armazena na variavel valorDesconto
    print("O valor a ser pago após o desconto é: R$", f"{valorDesconto:.2f}")
    # imprime na tela o valor a ser pago após o desconto, formatado com duas casas decimais
else:
    # caso o valor da compra seja maior que 300, entra neste bloco abaixo
    print("Voce recebeu um desconto de 15%") #imprime a mensagem "Voce recebeu um desconto de 15%" 
    valorDesconto = valorCompra * 0.85 # calcula o valor a ser pago após o desconto de 15% e 
     # armazena na variavel valorDesconto
    print("O valor a ser pago após o desconto é: R$", f"{valorDesconto:.2f}")
     # imprime na tela o valor a ser pago após o desconto, formatado com duas casas decimais
