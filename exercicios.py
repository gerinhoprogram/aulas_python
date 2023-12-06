nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    n = len(nome)
    letra = nome[0]

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido {nome[::-1]}')
    print(f'Seu nome tem {n} letras')
    print(f'A primeira letra é {letra}')

    if ' ' in nome:
        print('Com espaços')
    else:
        print('Sem espaços')

else:
    print(f'Campos vazios')