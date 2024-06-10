import time

def knapsack_recursive(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack_recursive(weights, values, capacity, n-1)
    else:
        return max(values[n-1] + knapsack_recursive(weights, values, capacity - weights[n-1], n-1),
                   knapsack_recursive(weights, values, capacity, n-1))

weights = [1, 2, 5, 8]
values = [2, 5, 6, 7]
capacity = 27
n = len(weights)
start_time = time.time()
result = knapsack_recursive(weights, values, capacity, n)
end_time = time.time()
print("Problema de la mochila\n")
print(f"Recursivo: Resultado = {result}, Tiempo = {end_time - start_time:.6f} segundos")
