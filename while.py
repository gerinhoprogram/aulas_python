nome = 'rogerio'

qtd_nome = len(nome)

indice = 0
nova_string = ''
while indice < len(nome):
    letra = nome[indice]
    nova_string += f'*{letra}'
    indice += 1

print(nova_string)