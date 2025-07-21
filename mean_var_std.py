import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError('List must contain nine numbers.')
    
    #convertir la matriz en 3x3
    matriz =np.array(lista).reshape(3, 3)
    
    #calcular la media
    mean_columns =matriz.mean(axis=0).tolist()
    mean_rows =matriz.mean(axis=1).tolist()
    mean_total =matriz.mean().item()
    
    #calcular variante
    var_columns =matriz.var(axis=0).tolist()
    var_rows =matriz.var(axis=1).tolist()
    var_total =matriz.var().item()
    
    #calcular la desvicion estandar
    std_columns =matriz.std(axis=0).tolist()
    std_rows =matriz.std(axis=1).tolist()
    std_total =matriz.std().item()
    
    #calcular maximo
    max_columns =matriz.max(axis=0).tolist()
    max_rows =matriz.max(axis=1).tolist()
    max_total =matriz.max().item()
    
    #calcular minimo
    min_columns =matriz.min(axis=0).tolist()
    min_rows =matriz.min(axis=1).tolist()
    min_total =matriz.min().item()
    
    #calcular suma
    sum_columns =matriz.sum(axis=0).tolist()
    sum_rows =matriz.sum(axis=1).tolist()
    sum_total =matriz.sum().item()
    
    
    calculations = {
        'mean': [mean_columns, mean_rows, mean_total],
        'variance': [var_columns, var_rows, var_total],
        'standard deviation': [std_columns, std_rows, std_total],
        'max': [max_columns, max_rows, max_total],
        'min': [min_columns, min_rows, min_total],
        'sum': [sum_columns, sum_rows, sum_total]
    }
    
    return calculations