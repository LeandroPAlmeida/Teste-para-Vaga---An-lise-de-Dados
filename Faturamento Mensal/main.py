import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def Media():
    with open('dados.json', 'r') as arq:
        conteudo = json.load(arq)
        SMensal = 0
        for dado in conteudo:
            Mvalor = dado['valor']
            SMensal += Mvalor
        c = len(conteudo)
        media = SMensal / c
    superiores = len([dado for dado in conteudo if dado['valor'] > media])
    SMensal_formatado = locale.currency(media, symbol=True, grouping=True)
    print(f'Quantidade de dias: {superiores} com a média de: {SMensal_formatado}.')

def Maior():
    with open('dados.json', 'r') as arq:
        conteudo = json.load(arq)
        Mvalor = 0
        for dado in conteudo:
            valor = dado['valor']
            if valor > Mvalor:
                Mvalor = valor
    Mvalor_formatado = locale.currency(Mvalor, symbol=True, grouping=True)
    print(f'O maior faturamento no mês foi de {Mvalor_formatado}.')

def Menor():
    with open('dados.json', 'r') as arq:
        conteudo = json.load(arq)
        Menor_valor = float('inf')
        for dado in conteudo:
            valor = dado['valor']
            if valor == 0:
                continue
            if valor < Menor_valor:
                Menor_valor = valor
    Menor_valor_formatado = locale.currency(Menor_valor, symbol=True, grouping=True)
    print(f'O menor faturamento no mês foi de {Menor_valor_formatado}.')

while True:
    print('-' * 30)
    print('Bem Vindo')
    print('Em que posso lhe ajudar hoje?')
    print('-' * 30)
    opcao = int(input('0 - O maior valor faturado no mês\n'
                      '1 - O menor valor faturado no mês\n'
                      '2 - Quantos dias no mês o faturamento foi superior a média mensal\n'
                      '3 - Sair\n'))

    if opcao == 0:
        Maior()
    elif opcao == 1:
        Menor()
    elif opcao == 2:
        Media()
    elif opcao == 3:
        print('Até mais!!')
        break
    else:
        print('\033[91mOpção Inválida!! Tente Novamente.\033[0m')
