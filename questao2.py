# Variáveis:
# preço BA, tamanhos p, m e g
precoBp = 16.00
precoBm = 18.00
precoBg = 22.00

# preço FF, tamanhos p, m e g
precoFp = 15.00
precoFm = 17.00
precoFg = 21.00

precoTotal = 0

# Menu:
print('-' * 10, 'Bem-vindo a loja do Alex Lopes Quintela', '-' * 9)
print('-' * 25, 'Cardápio', '-' * 25 + '\n' + '-' * 60)
print('----| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |---')
print(f'----|    P    |      R$ {precoBp:.2f}      |      R$ {precoFp:.2f}      |---')
print(f'----|    M    |      R$ {precoBm:.2f}      |      R$ {precoFm:.2f}      |---')
print(f'----|    G    |      R$ {precoBg:.2f}      |      R$ {precoFg:.2f}      |---' + '\n' + '-' * 60)


# Programa Principal:
while True:
    # Pergunta sabor:
    sabor = input('Digite o sabor desejado (BA/FF): ').lower().strip()
    if sabor != 'ba' and sabor != 'ff':
        print('Sabor inválido. Tente novamente\n')
        continue

    # Pergunta tamanho:
    tamanho = input('Digite o tamanho desejado (P/M/G): ').lower().strip()
    if len(tamanho) != 1 and tamanho not in 'pmg' or tamanho == '':
        print('Tamanho inválido. Tente novamente\n')
        continue

    # Precifica o pedido de Bife Acebolado, dependendo do tamanho:
    if sabor == 'ba':
        if tamanho == 'p':
            print(f'Você pediu um Bife Acebolado no tamanho {tamanho.upper()}: R$ {precoBp}\n')
            precoTotal += precoBp
        else:
            if tamanho == 'm':
                print(f'Você pediu um Bife Acebolado no tamanho {tamanho.upper()}: R$ {precoBm}\n')
                precoTotal += precoBm
            else:
                if tamanho == 'g':
                    print(f'Você pediu um Bife Acebolado no tamanho {tamanho.upper()}: R$ {precoBg}\n')
                    precoTotal += precoBg

    # Precifica o pedido de Filé de Frango, dependendo do tamanho:
    else:
        if tamanho == 'p':
            print(f'Você pediu um Filé de Frango no tamanho {tamanho.upper()}: R$ {precoFp}\n')
            precoTotal += precoFp
        else:
            if tamanho == 'm':
                print(f'Você pediu um Filé de Frango no tamanho {tamanho.upper()}: R$ {precoFm}\n')
                precoTotal += precoFm
            else:
                if tamanho == 'g':
                    print(f'Você pediu um Filé de Frango no tamanho {tamanho.upper()}: R$ {precoFg}\n')
                    precoTotal += precoFg

    continuar = input('Deseja pedir mais alguma coisa? (S/N): ').lower().strip()
    while continuar != 's' and continuar != 'n':
        continuar = input('Deseja pedir mais alguma coisa? (S/N): ').lower().strip()

    if continuar == 's':
        continue
    else:
        print(f'\nO valor total a ser pago é: R$ {precoTotal:.2f}')
        break
