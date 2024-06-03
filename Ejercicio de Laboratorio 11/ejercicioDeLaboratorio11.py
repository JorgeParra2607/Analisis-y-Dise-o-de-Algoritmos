def contar_rutas(laberinto):
    m = len(laberinto)
    n = len(laberinto[0])
    
    # Si la celda inicial o la final son obstaculos, no hay rutas posibles
    if laberinto[0][0] == 1 or laberinto[m-1][n-1] == 1:
        return 0
    
    # Matriz de DP para almacenar el numero de rutas
    dp = [[0] * n for _ in range(m)]
    
    # Inicializamos el punto de partida
    dp[0][0] = 1
    
    # Rellenamos la matriz de DP
    for i in range(m):
        for j in range(n):
            if laberinto[i][j] == 0:
                if i > 0:
                    dp[i][j] += dp[i-1][j]  
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]

# Ejemplo de uso
laberinto = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print('\n', contar_rutas(laberinto))
