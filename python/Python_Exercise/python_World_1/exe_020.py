from random import shuffle
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'a ordem da apresentacção sera \n\033[31;40m{lista}\033[m')
