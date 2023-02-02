def horasTrabalhada():

    ganhos_por_hora = float(input('Digite seus ganhos por hora: '))
    numeros_de_horas_por_mes = int(input('Digite a quantidade de horas: '))

    salario = ganhos_por_hora * numeros_de_horas_por_mes

    print(f'Seu salário por mês é: R$ {salario:.2f}')

horasTrabalhada()
