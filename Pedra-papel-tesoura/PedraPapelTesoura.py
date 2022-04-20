import random

x = input('Olá, gostaria de jogar? (s/n): ')

while x == 's' or x == 'S':
    print('Bem vindo ao jogo Pedra, papel e tesoura')
    print('Hoje jogaremos juntos e veremos quem será o mais sortudo')

    print('primeiramente, escolha uma opção entre: \n1. pedra \n2. papel \n3. tesoura')

    escolha = int(input())

    while escolha > 3 or escolha < 1:
        escolha = int(input('insira uma opção válida: '))

    if escolha == 1:
        escolha = 'pedra'
        print('parabéns! você escolheu pedra \nagora é a vez do computador')
    if escolha == 2:
        escolha = 'papel'
        print('parabéns! você escolheu papel \nagora é a vez do computador')
    if escolha == 3:
        escolha = 'tesoura'
        print('parabéns! você escolheu tesoura \nagora é a vez do computador')

    escolha_comp = random.randint(1, 3)
    
    if escolha_comp == 1:
        escolha_comp = 'pedra'
    elif escolha_comp == 2:
        escolha_comp = 'papel'
    elif escolha_comp == 3:
        escolha_comp = 'tesoura'
        
    while escolha_comp == escolha:
        escolha_comp = random.randint(1, 3)
        if escolha_comp == 1:
            escolha_comp = 'pedra'
        elif escolha_comp == 2:
            escolha_comp = 'papel'
        elif escolha_comp == 3:
            escolha_comp = 'tesoura'

    print(f'o computador escolheu: {escolha_comp} \nagora vamos jogar')

    if escolha == 'pedra' and escolha_comp == 'tesoura':
        print('embate: pedra vs. tesoura \nparabéns! o usuário derrotou o computador')
    elif escolha == 'pedra' and escolha_comp == 'papel':
        print('embate: pedra vs. papel \ncomputador é o vencedor!')
    elif escolha == 'papel' and escolha_comp == 'pedra':
        print('embate: papel vs pedra \nparabéns! o usuário derrotou o computador')
    elif escolha == 'papel' and escolha_comp == 'tesoura':
        print('embate: papel vs tesoura \ncomputador é o vencedor!')
    elif escolha == 'tesoura' and escolha_comp == 'pedra':
        print('embate: tesoura vs pedra \ncomputador é o vencedor!')
    elif escolha == 'tesoura' and escolha_comp == 'papel':
        print('embate: tesoura vs papel \nparabéns! o usuário derrotou o computador')
    x = input('gostaria de jogar novamente? (s/n): ')

print('fim')
