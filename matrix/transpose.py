def transpose(matrix):
    """
    Transpone una matriz intercambiando filas por columnas.

    Args:
        matrix: Lista bidimensional de enteros

    Returns:
        Lista bidimensional con la matriz transpuesta
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

    # Para matrices NxM generales usando list comprehension
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

    return transposed
