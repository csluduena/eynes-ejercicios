def transpose(matrix):
    """
    Transpone una matriz intercambiando filas por columnas.
    Implementación inicial para casos básicos.
    """
    if not matrix or not matrix[0]:
        return []
    
    # Para matriz 1x1
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix
    
    # Para matriz 1xN (una fila, N columnas) -> NX1 (N filas, 1 columna)
    if len(matrix) == 1:
        return [[matrix[0][i]] for i in range(len(matrix[0]))]
    
    # Para matriz Nx1 (N filas, 1 columna) -> 1xN (1 fila, N columnas)
    if len(matrix[0]) == 1:
        return [[matrix[i][0] for i in range(len(matrix))]]
    
    # Para casos más complejos, retornamos None por ahora
    return None
