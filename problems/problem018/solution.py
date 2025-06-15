def max_path_sum(triangle):
    if not triangle:
        return 0

    # Hacemos una copia del triángulo para no modificar el original
    tri = [row[:] for row in triangle]

    # Desde la penúltima fila hacia arriba
    for row in range(len(tri) - 2, -1, -1):
        for col in range(len(tri[row])):
            tri[row][col] += max(tri[row + 1][col], tri[row + 1][col + 1])
    
    return tri[0][0]  # El resultado final está en la cima
