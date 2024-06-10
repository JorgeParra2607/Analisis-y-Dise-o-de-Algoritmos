import time

def knapsack_tabular(weights, values, capacity, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][w]

weights = [1, 2, 5, 8]
values = [2, 5, 6, 7]
capacity = 27
n = len(weights)
start_time = time.time()
result = knapsack_tabular(weights, values, capacity, n)
end_time = time.time()
print("Problema de la mochila\n")
print(f"Tabular: Resultado = {result}, Tiempo = {end_time - start_time:.6f} segundos")
