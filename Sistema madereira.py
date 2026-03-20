def escolha_tipo(): #função do tipo
    print('Bem vindo ao Madeireira do Gustavo Amaral🪵')
    print('\nQual tipo de madeira você deseja?: ')
    print('PIN - Tora de Pinho')
    print('PER - Tora de Peroba')
    print('MOG - Tora de Mogno')
    print('IPE - Tora de Ipê')
    print('IMB - Tora de Imbuia')

    while True:#laço do tipo de madeira
        tipo = input('>>').upper()
        if tipo == 'PIN':
           return 150.40
        elif tipo == 'PER':
           return 170.20
        elif tipo == 'MOG':
           return 190.90
        elif tipo == 'IPE':
           return 210.10
        elif tipo == 'IMB':
           return 220.70
        else:
            print('Escolha inválida!, entre com o tipo novamente!') #invalida o tipo que não corresponda com as opões
def qtd_toras():

    print('\nescolha a quantidade de toras (m³): ')
    while True:#laço das quantidades de toras
        try:
            qtd = float(input('Quantas toras? '))
            if qtd > 2000:
                print('não aceitamos pedidos com essa quantidade de toras!') #invalida o pedido acima do limite
            elif qtd >= 1000:
                return qtd, 16/100
            elif qtd >= 500:
                return qtd, 9/100
            elif qtd >= 100:
                return qtd, 4/100
            else:
                return qtd, 0
        except:
            print('valor inválido!')

def transporte():
    print('\nEscolha o tipo de transporte: ')
    print('1 - Transoporte rodoviário - R$ 1000.00')
    print('2 - Transporte Ferroviário - R$ 2000.00')
    print('3 - Transporte Hidroviário - R$ 2500.00')
    while True:#laço do transporte
        try:
            opçao = (input('>> '))
            if opçao == '1':
                return 1000.00
            elif opçao == '2':
                return 2000.00
            elif opçao == '3':
                return 2500.00
            else:
                print('opção invalida!')
        except:
            print('valor invalido!')
#principal abaixo
tipoMadeira = escolha_tipo()
qtd, desconto = qtd_toras()
frete = transporte()

total = (tipoMadeira * qtd) * (1 - desconto) + frete #calcula o total
print(f'total do seu pedido: R$ {total:.2f}')
print('obrigado pela preferência!!🪵🪓')







