while True:

    n1 = input('Número 1: ')
    n2 = input('Número 2: ')
    operador = input('Operador (+-/*): ')

    validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        validos = True

    except:
        validos = None

    if validos is None:
        print('Um dos números é inválido.')

        # volta para o loop
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    
    print('Realizando sua conta')

    if operador == '+':
        print(n1_float + n2_float)
    elif operador == '-':
        print(n1_float - n2_float)
    elif operador == '/':
        print(n1_float / n2_float)
    elif operador == '*':
        print(n1_float * n2_float)

    # -----------
    sair = input('Sair do sistema? [s]im: ').lower().startswith('s')

    if sair:
        break