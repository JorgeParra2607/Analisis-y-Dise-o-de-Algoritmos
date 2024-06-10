import time

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        res = coin_change_recursive(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    return min_coins

coins = [1, 2, 5, 7, 11]
amount = 26
start_time = time.time()
result = coin_change_recursive(coins, amount)
end_time = time.time()
print(f"Problema del cambio\n")
print(f"Recursivo: Resultado = {result}, Tiempo = {end_time - start_time:.6f} segundos")
