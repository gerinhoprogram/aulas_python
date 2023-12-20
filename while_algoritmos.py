frase = 'Uma frase qualquer bbbdbdbdbdb'

i=0
qtd_apareceu_mais = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd = frase.count(letra_atual)

    if qtd_apareceu_mais < qtd:
        qtd_apareceu_mais = qtd
        letra_mais_vezes = letra_atual

    i+=1

print('A letra que apareceu mais foi '
      f'{letra_mais_vezes} que apareceu'
      f'{qtd_apareceu_mais}x')

