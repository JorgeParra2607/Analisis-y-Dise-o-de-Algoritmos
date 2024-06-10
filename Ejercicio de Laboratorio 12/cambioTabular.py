import time

def coin_change_tabular(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5, 7, 11]
amount = 26
start_time = time.time()
result = coin_change_tabular(coins, amount)
end_time = time.time()
print("Problema del cambio\n")
print(f"Tabular: Resultado = {result}, Tiempo = {end_time - start_time:.6f} segundos")
