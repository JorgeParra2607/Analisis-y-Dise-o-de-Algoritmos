import time

def knapsack_memo(weights, values, capacity, n, memo=None):
    if memo is None:
        memo = {}
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        memo[(n, capacity)] = knapsack_memo(weights, values, capacity, n-1, memo)
    else:
        memo[(n, capacity)] = max(values[n-1] + knapsack_memo(weights, values, capacity - weights[n-1], n-1, memo),
                                  knapsack_memo(weights, values, capacity, n-1, memo))
    return memo[(n, capacity)]

weights = [1, 2, 5, 8]
values = [2, 5, 6, 7]
capacity = 27
n = len(weights)
start_time = time.time()
result = knapsack_memo(weights, values, capacity, n)
end_time = time.time()
print("Problema de la mochila\n")
print(f"Memoizado: Resultado = {result}, Tiempo = {end_time - start_time:.6f} segundos")
