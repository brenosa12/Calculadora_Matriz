from time import sleep
def calculo(ord, m1, m2, mf):
    if ord == 0:
        for l in range(0, lin):
            for c in range(0, col):
                d = m1[l][c] - m2[l][c]
                mf.append(d)
            print(*mf, sep=' ')
            mf.clear()
    elif ord == 1:
        for l in range(0, lin):
            for c in range(0, col):
                d = m1[l][c] + m2[l][c]
                mf.append(d)
            print(*mf, sep=' ')
            mf.clear()


seletor = int(input('Digite 0 - Para fazer a Subtração das matrizes.\nDigite 1 - Para fazer a Adição das matrizes.\n'))
lin = int(input('Digite a quantidade de linhas da matriz: '))
col = int(input('Digite a quantidade de colunas da matriz: '))
matriz1 = []
matriz2 = []
matrizfinal = []
print(' Digite a Primeira Matriz:')
for i in range(lin):
    linha = [int(x) for x in input().split()]
    matriz1.append(linha)
print('Digite a Segunda Matriz:')
for z in range(lin):
    linha2 = [int(x) for x in input().split()]
    matriz2.append(linha2)
print('CALCULANDO...')
sleep(2)
print('Resultado:')
print('=-='*10)
calculo(seletor, matriz1, matriz2, matrizfinal)
print('=-='*10)