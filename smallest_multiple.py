import numpy as np

##232792560
cant_evaluate = 20
num_validate = cant_evaluate
while True:
    modulo_array = num_validate%np.arange(1,cant_evaluate +1)
    if modulo_array.sum() != 0:
        num_validate += cant_evaluate
    else: 
        print(f'Cumple y el número es {num_validate}')
        break