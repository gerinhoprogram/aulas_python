number_str = input(
    'Dobrar numero: '
)

try:
    number_float = float(number_str)
    print(f'O dobro de {number_str} é {number_float * 2}')
except:
    print(f'Não é numero')

# if number_str.isdigit():
#     number_float = float(number_str)
#     print(f'O dobro de {number_str} é {number_float * 2}')
# else:
#     print(f'Não é numero')