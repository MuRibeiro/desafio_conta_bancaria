menu = f'''
                            ==========================
                            =     BANCO - PYTHON     =
                            ==========================
                            = 1 - DEPÓSITO           =
                            = 2 - SAQUE              =
                            = 3 - EXTRATO            =
                            = 4 - SAIR               =
                            ==========================
'''
saldo = 0
LIMITE_VALOR = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor do depósito: R$"))

        if valor > 0:
            saldo += valor
            extrato += f'+R${valor:.2f}\n'
            print(f'Saldo: R${saldo}')

        else:
            print('Informe um valor né fi!')

    elif opcao == '2':
        if numero_saques < LIMITE_SAQUE:
            print(f'Saldo: R${saldo}')
            saque = float(input('Informe o valor do saque: R$'))
            if saque <= LIMITE_VALOR:
                if saldo >= saque:
                    numero_saques += 1
                    extrato +=f'-R${saque}\n'
                    print('Saque efetuado com sucesso!')
                    saldo = saldo - saque
                    print(f'Saldo: R${saldo}')
                else:
                    print('Saldo insuficiente!')
            else:
                print(f'Saque não permitido. Seu limite diario é R${LIMITE_VALOR}')
        else:
            print('Limite de saque atingido!')

    elif opcao == '3':
        print(extrato)
        print(f'Saldo: R${saldo}')

    elif opcao == '4':
        print('BANCO PYTHON AGRADECE A PREFERÊNCIA!')
        break
    else:
        print('DIGITE UMA OPÇÃO VALÍDA, BURRO!')
