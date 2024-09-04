import os
import time

entrada = int(input('Insira um número inteiro positivo: '))

if entrada > 0:
        print('Contagem regressiva...')
        while entrada > 0:
            print(entrada)
            entrada += -1
            time.sleep(1)
            os.system('cls')
        print('Boooom')
    

