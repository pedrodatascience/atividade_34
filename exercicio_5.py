# Lista com 10 nomes
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo',
         'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana']

indice = int(input('Informe um índice: '))

print(nomes[indice] if indice >= 0 and indice < 10 else 'Índice inexistente.')