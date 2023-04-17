faturamento = {'SP': 6783643, 'RJ': 3667866, 'MG': 2922988, 'ES': 2716548, 'Outros': 1984953}

total = sum(faturamento.values())

print('Percentual de cada estado no mês:')

for estado, valor in faturamento.items():
    porcentagem = (valor / total) * 100
    print(f"{estado}: {porcentagem:.2f}%")

