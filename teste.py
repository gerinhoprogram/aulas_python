string = 'rogerio  furquim'
outra = f'{string[:3]}'

#print(string.zfill(20))

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Pula o 6')
        continue

    if contador >= 20 and contador <= 30:
        print('Pular do 20 ao 30')
        continue

    print(contador)

    if contador == 90:
        break
    

print('fim')